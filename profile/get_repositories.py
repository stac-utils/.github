import json
from pathlib import Path

import requests
from requests import Response

here = Path(__file__).parent


def get(url: str) -> Response:
    return requests.get(
        url=url,
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )


repositories = list()
url = "https://api.github.com/orgs/stac-utils/repos"
while True:
    response = get(url)
    repositories.extend(response.json())
    if "next" in response.links:
        url = response.links["next"]["url"]
    else:
        break

repositories.sort(key=lambda r: r["stargazers_count"], reverse=True)

with open(here / "repositories.json", "w") as f:
    json.dump(repositories, f)
