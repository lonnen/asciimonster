# asciimonster

a cli tool for ingesting a file and vomiting out ascii character stats.

This is not intended to be a robust or general tool. It can probably be replaced with a bash one-liner. This is a quick 'n dirty tool for deriving a dataset to help with solving the [cryptopals](https://www.cryptopals.com/) challenge sets.

The Project Gutenberg text of Don Quixote is included in the `data/` folder and licensed under the Project Gutenberg License.

## Installation

Install this tool using `pip`:
```bash
pip install asciimonster
```
## Usage

```bash
asciimonster data/pg996.txt
```

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
