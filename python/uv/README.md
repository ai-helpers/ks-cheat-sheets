#  Cheat Sheet - UV Python package manager

# Table of Contents (ToC)
- [Cheat Sheet - UV Python package manager](#cheat-sheet---uv-python-package-manager)
- [Table of Contents (ToC)](#table-of-contents-toc)
- [References](#references)
- [UV](#uv)
  - [Installation](#installation)
  - [Features](#features)
  - [Differences with poetry](#differences-with-poetry)


# References
- [UV Documentation - Installation methods](https://docs.astral.sh/uv/getting-started/installation/#installation-methods)
- [UV Documentation - Uninstallation](https://docs.astral.sh/uv/getting-started/installation/#uninstallation)
- [Loopwerk article (September, 2024) - python poetry vs uv](https://www.loopwerk.io/articles/2024/python-poetry-vs-uv/)
- [Loopwerk article (October 04, 2024) - Trying out PDM (and comparing it with Poetry and uv)](https://www.loopwerk.io/articles/2024/trying-pdm/)
- [Loopwerk article (November 11, 2024) - Python uv revisited](https://www.loopwerk.io/articles/2024/python-uv-revisited/)

# UV
## Installation

Installation
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
uv --help
```

## Features

[Documentation sources](https://docs.astral.sh/uv/getting-started/features/)

Python versions management
Installing and managing Python itself.

```sh
uv python install: Install Python versions.
uv python list: View available Python versions.
uv python find: Find an installed Python version.
uv python pin: Pin the current project to use a specific Python version.
uv python uninstall: Uninstall a Python version.
```

## Differences with poetry

```sh
$ poetry init
$ poetry add django
$ poetry add ruff --group dev
$ poetry install --with dev
$ poetry run ./manage.py
```

```sh
$ uv init
$ uv add django
$ uv add ruff --dev
$ uv run ./manage.py
```