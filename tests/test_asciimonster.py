from click.testing import CliRunner
from asciimonster.__main__ import asciimonster

def test_asciimonster():
    runner = CliRunner()
    result = runner.invoke(asciimonster, ["data/pg996.txt"])
    assert result.exit_code == 0
    lines = result.output.strip().split("\n")
    assert len(lines) == 95
    assert lines[0].startswith("32")
    assert lines[-1].startswith("126")
