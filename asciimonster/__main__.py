from collections import Counter

import click

@click.command()
@click.argument("input", type=click.File("rb"))
def asciimonster(input):
    "a cli tool for ingesting a file and vomiting out ascii character stats"
    characters = Counter()
    while True:
        c = input.read(1)
        if not c:
            break
        characters.update([c])
        click.echo(c)


if __name__ == "__main__":
    asciimonster()
