import click

VALID_MODES = click.Choice(["name"], False)
VALID_NAME_GENERATORS = click.Choice(["project"], False)
VALID_IDEA_GENERATORS = click.Choice(["game"], False)

@click.group()
def CLI():
    pass

@CLI.command('name', help="Generates a name.")
@click.argument('generator', type=VALID_NAME_GENERATORS)
@click.argument('amount', type=int)
def name(generator: str = "", amount = 1):
    print(generator)

@CLI.command('idea', help = "Generates an idea/concept.")
@click.argument('generator', type=VALID_IDEA_GENERATORS)
@click.argument('amount', type=int)
def name(generator: str = "", amount = 1):
    print(generator)

if __name__ == "__main__":
    CLI()