# asciimonster

[![PyPI](https://img.shields.io/pypi/v/asciimonster.svg)](https://pypi.org/project/asciimonster/)
[![Changelog](https://img.shields.io/github/v/release/lonnen/asciimonster?include_prereleases&label=changelog)](https://github.com/lonnen/asciimonster/releases)
[![Tests](https://github.com/lonnen/asciimonster/actions/workflows/test.yml/badge.svg)](https://github.com/lonnen/asciimonster/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/lonnen/asciimonster/blob/master/LICENSE)

a cli tool for ingesting a file and vomiting out ascii character stats

## Installation

Install this tool using `pip`:
```bash
pip install asciimonster
```
## Usage

For help, run:
```bash
asciimonster --help
```
You can also use:
```bash
python -m asciimonster --help
```
## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:
```bash
cd asciimonster
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
