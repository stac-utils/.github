# stac-utils

Implementations and tooling for the [STAC specification](https://stacspec.org/).

## Diagram

This is a high-level diagram of some, but not all, repos in **stac-utils**, mostly focused on Python.
A Javascript version of this diagram is WIP (<https://github.com/stac-utils/.github/issues/2>).
Repos are sorted into three categories:

- **Producers**: Used to create STAC metadata, particularly for large, public datasets
- **Servers**: Used to serve STAC metadata via a [STAC API](https://github.com/radiantearth/stac-api-spec)
- **Consumers**: Used to consume, download, and analyze STAC metadata and their referenced assets

This diagram was initially presented at the [2023 STAC Sprint](https://github.com/radiantearth/community-sprints/tree/main/09262023-philadelphia-pa).

![stac-utils](https://raw.githubusercontent.com/stac-utils/.github/main/drawings/stac-utils.png)
