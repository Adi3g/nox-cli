import click


@click.group()
def cli():
    """Nox CLI tool."""
    pass

@cli.command()
def init():
    """Initialize the nox project."""
    click.echo('Initializing nox...')

if __name__ == '__main__':
    cli()
