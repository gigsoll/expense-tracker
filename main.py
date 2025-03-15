import click


@click.group()
def cli() -> None:
    pass


@click.command()
@click.argument("description", type=str)
@click.argument("amount", type=int)
@click.option("--category", type=str)
def add(description: str, amount: str, category: str) -> None:
    """Add new expence to expence tracker"""
    pass


@click.command()
@click.option("--description", type=str)
@click.option("--amount", type=float)
@click.option("--category", type=str)
def update(description: str, amount: float, category: str) -> None:
    """Update expence by ID"""
    pass


@click.command()
@click.argument("id", type=int)
def delete(id: int) -> None:
    """Delete expence by ID"""
    pass


@click.command()
def show() -> None:
    """Display all the expences"""
    pass


@click.command()
@click.option("--month",
              type=int,
              help="Spending amount per specific month of current year")
@click.option("--year",
              type=int,
              help="Spending amount per specific year")
@click.option("--all",
              is_flag=True,
              help="Total sum of spending")
def summary(mount: int, all: bool) -> None:
    """Show total sum of expences per year, month or all time"""
    pass


cli.add_command(add)
cli.add_command(update)
cli.add_command(delete)
cli.add_command(summary)
cli.add_command(show)


if __name__ == "__main__":
    cli()
