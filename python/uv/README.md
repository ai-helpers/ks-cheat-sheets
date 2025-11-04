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

## Main features

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


## Creating projects

```sh
uv init # initialise a project in the current directory
uv init # init a project myproj in the directory myproj
uv init # init a packageable app 
uv init # init a packageable library
uv init # use python 3.X for your project
```

## Managing project dependencies

```sh
uv add requests # add requests as a dep
uv add -r requirements.txt # add dep form the file requirements.txt
uv add --dev pytest # add pytest as a dev dep
uv run pytest # run pytest executable that is installed in your project
uv remove requests # remove request as a dep
uv tree # see the project dep tree
uv lock --upgrade # upgrade the dep versions
```

## Project lifecycle management

```sh
uv build # build your packageable project
uv publish # publish your packageable project to pypi
uv version # check you project version 
uv version --bump major # bump ,project major version
uv version --bump minor --bump beta # bump minor version into a beta
uv version --bump rc # bump version into release candidate
uv version --bump stable # turn into a stable version
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
