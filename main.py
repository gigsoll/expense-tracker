import os
import click
from datetime import datetime as dt
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
        res = em.add(Expence(description, amount))
    else:
        cat = get_category(category)
        res = em.add(Expence(description, amount, category=cat))
    click.echo(res)


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
@click.option("--category", type=str)
def show(category) -> None:
    """Display all the expences"""
    if category:
        category = get_category(category)
        result = em.show_by_category(category)
    else:
        result = em.show()
    click.echo(result)


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

    if all:
        total = em.total_expence()
    else:
        total = em.total_by_time(month, year)
    click.echo(f"Money spent: {total}")


@click.command()
@click.argument("path", type=click.Path())
@click.option("--name", type=str)
def export(path, name: str):
    """Exports your expences to .csv format"""
    is_dir = os.path.isdir(path)
    if is_dir and not name:
        filename = int(round(dt.timestamp(dt.now()) * 10**3))
        name = str(filename) + ".csv"
    split_name: list[str] = name.split(".")
    if name and split_name[-1] != "csv":
        split_name.append("csv")
        name = '.'.join(split_name)
    pretty: list[dict] = em._to_pretty_dict()

    try:
        with open(os.path.join(path, name), "w", encoding="utf-8") as ds:
            ds.write(";".join(list(pretty[0].keys())) + "\n")
            for el in pretty:
                ds.write(";".join([str(el) for el in el.values()]) + "\n")
    except FileNotFoundError:
        print("File not found")
    except NotADirectoryError:
        print("You should write file into an existing directory")


@click.command()
@click.argument("amount", type=int)
def limit(amount):
    """Change your limit amount"""
    em.update_limit(amount)


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
cli.add_command(export)
cli.add_command(limit)


if __name__ == "__main__":
    cli()
