"""Command version."""

import click
from typing import Dict, List
from .. import __version__


# If you consider your work is important enough (decided by yourself), put
# yourself into this dictionary.
CREDITS: Dict[str, List[str]] = {"Author": ["Yi Cao"]}


@click.command()
@click.option("-c", "--credits", is_flag=True, help="Show credits")
def version(credits: bool):
    """Show the current version of cfpm."""
    click.echo(
        "cfpm version " + click.style(str(__version__), fg="bright_blue")
    )
    if credits:
        print()
        for (key, value) in CREDITS.items():
            print(key)
            for name in value:
                print("  " + name)
