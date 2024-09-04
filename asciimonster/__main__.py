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
    for i in range(32, 127):
        count = characters.get(chr(i), 0)
        frequency = "{0:.{1}f}".format((count / total * 100), 2)
        line = ", ".join([str(i), chr(i), str(count), frequency])
        click.echo(line)


if __name__ == "__main__":
    asciimonster()
