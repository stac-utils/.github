import json
from pathlib import Path
from typing import Any

import jinja2
import tomllib
from jinja2 import Environment, PackageLoader

IGNORE = [".github", "developer-guide", "pgstacrs"]

here = Path(__file__).parent

with open(here / "config.toml", "rb") as f:
    config = tomllib.load(f)

with open(here / "repositories.json") as f:
    repositories = json.load(f)

for repository in repositories:
    if repository["name"] in IGNORE or repository["archived"]:
        continue
    seen = False
    for category in config["categories"].values():
        if repository["name"] in category:
            seen = True
    if not seen:
        raise Exception(f"repository is not categorized: {repository['name']}")

config["repositories"] = repositories

environment = Environment(
    loader=PackageLoader("render"), autoescape=jinja2.select_autoescape()
)


def category_filter(
    repositories: dict[str, list[str]], category: str
) -> list[dict[str, Any]]:
    names = config["categories"][category]
    return [r for r in repositories if r["name"] in names]


def is_for(repository: dict[str, Any], user: str) -> bool:
    return repository["name"] in config[f"for-{user}"]


def check(value: bool) -> str:
    if value:
        return "✅"
    else:
        return ""


environment.filters["category"] = category_filter
environment.filters["is_for"] = is_for
environment.filters["check"] = check
table = environment.get_template("table.md.jinja2")


def table_filter(repositories: list[dict[str, Any]]) -> str:
    return table.render({"repositories": repositories})


environment.filters["table"] = table_filter
template = environment.get_template("README.md.jinja2")
with open(here / "README.md", "w") as f:
    f.write(template.render(config))
