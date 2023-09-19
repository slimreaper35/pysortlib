# Python Sorting Library

[![PyPI](https://img.shields.io/pypi/v/pysortlib)](https://pypi.org/project/pysortlib)
[![Downloads](https://static.pepy.tech/badge/pysortlib)](https://pepy.tech/project/pysortlib)
[![Coverage](https://coveralls.io/repos/github/slimreaper35/pysortlib/badge.svg?branch=main)](https://coveralls.io/github/slimreaper35/pysortlib?branch=main)

**Sorting algorithms**

- Insert sort
- Bubble sort
- Merge sort
- Selection sort
- Quick sort
- Heap sort
- Counting sort
- Radix sort

Each sorting algorithm contains a precise implementation with documented time and space complexity.

## Install

```bash
pip install pysortlib
```

## Usage

```python
from pysortlib import insert_sort

array = [3, 5, 2, 1, 7, 4, 6]
insert_sort(array)  # set a breakpoint and explore \o/
print(array)
```

## Development

#### Virtual environment

```bash
pip install --user poetry
poetry config virtualenvs.in-project true
poety shell
poetry install
```

#### Pre-commit

```bash
pre-commit clean
pre-commit install --hook-type pre-commit
pre-commit autoupdate
```

#### Depenedencies

```bash
poetry update
poetry export --with dev --output requirements-dev.txt
```

#### SBOM

```bash
cyclonedx-py --poetry --format json --purl-bom-ref --output bom.json --force
```

#### Coding standards

- ~~perfectionism~~
- [black](https://black.readthedocs.io/en/stable/) - code formatting
- [ruff](https://beta.ruff.rs/docs/) - static code analysis
- [mypy](https://mypy.readthedocs.io/en/stable/) - static type checking
- [pytest](https://docs.pytest.org/en/stable/) - unit tests

## License

This project is licensed under the terms of the MIT license.
