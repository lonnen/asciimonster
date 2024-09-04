from collections import Counter

import click


@click.command()
@click.argument("input", type=click.File("r"))
def asciimonster(input):
    "a cli tool for ingesting a file and vomiting out ascii character stats"
    characters = Counter()
    while True:
        c = input.read(1)
        if not c:
            break
        characters.update([c])

    total = float(characters.total())
    stats = sorted(
        [(ord(char), char, count, count / total) for char, count in characters.items()]
    )
    for line in [s for s in stats if s[0] < 256 and s[0] > 30]:
        click.echo(", ".join([str(item) for item in line]))


if __name__ == "__main__":
    asciimonster()
