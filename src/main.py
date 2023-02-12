import click

VALID_MODES = click.Choice(["name"], False)
VALID_NAME_GENERATORS = click.Choice(["project"], False)
VALID_IDEA_GENERATORS = click.Choice(["game"], False)

@click.group()
def CLI():
    pass

@CLI.command('name')
@click.argument('generator', type=VALID_NAME_GENERATORS)
def name(generator: str = ""):
    print(generator)

@CLI.command('idea')
@click.argument('generator', type=VALID_IDEA_GENERATORS)
def name(generator: str = ""):
    print(generator)

if __name__ == "__main__":
    CLI()