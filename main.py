import click
from classes.Categories import Categories
from classes.Category import Category
from classes.Expence import Expence
from expence_manager import ExepnceManager
em = ExepnceManager()


@click.group()
def cli() -> None:
    pass


@click.command()
@click.argument("description", type=str)
@click.argument("amount", type=float)
@click.option("--category", type=str)
def add(description: str, amount: float, category: str) -> None:
    """Add new expence to expence tracker"""
    if not category:
        em.add(Expence(description, amount))
    else:
        cat = get_category(category)
        em.add(Expence(description, amount, category=cat))
    click.echo(f"New expence '{description}' added")


@click.command()
@click.argument("id", type=int)
@click.option("--description", type=str)
@click.option("--amount", type=float)
@click.option("--category", type=str)
def update(id: int, description: str, amount: float, category: str) -> None:
    """Update expence by ID"""
    cat = get_category(category) if category else None
    em.update(id, description, amount, cat)


@click.command()
@click.argument("id", type=int)
def delete(id: int) -> None:
    """Delete expence by ID"""
    click.echo(em.delete(id))


@click.command()
def show() -> None:
    """Display all the expences"""
    click.echo(em.show())


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
def summary(month: int, year: int, all: bool) -> None:
    """Show total sum of expences per year, month or all time"""
    total: float = 0
    if year:
        total = em.total_by_time("year", year)
    elif month:
        total = em.total_by_time("month", month)
    elif all:
        total = em.total_expence()
    click.echo(f"Money spent: {total}")


def get_category(category: str) -> Category:
    availible: list[Category] = [cat.value for cat in Categories]
    cat: Category
    for cat in availible:
        if cat.name == category:
            return cat
    return Categories.OTHER.value


cli.add_command(add)
cli.add_command(update)
cli.add_command(delete)
cli.add_command(summary)
cli.add_command(show)


if __name__ == "__main__":
    cli()
