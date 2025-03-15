import os
import json
from tabulate import tabulate
from datetime import datetime
from typing import Any
from dataclasses import asdict
from classes.Expence import Expence
from platformdirs import user_cache_dir
from classes.Categories import Categories
from classes.Category import Category, Group


class ExepnceManager():
    def __init__(self) -> None:
        self.expence_list: list[Expence] = []
        self.cahcedir = user_cache_dir("expence_tracker", "gigsoll")
        self.expence_file = os.path.join(self.cahcedir, "expences.json")
        self.read_file()

    def write_file(self) -> None:
        data = json.dumps(
            [asdict(exp) for exp in self.expence_list],
            indent=4
        )
        with open(self.expence_file, "w") as expence_file:
            expence_file.write(data)

    def add(self, expence: Expence) -> None:
        self.expence_list.append(expence)
        self.write_file()

    def delete(self, id) -> str:
        expence: Expence
        for expence in self.expence_list:
            if expence.id == id:

                self.expence_list.remove(expence)
                self.write_file()
                return f"Expence with id {id} was removed"
        return f"Expence with id {id} wasn't found"

    def show(self) -> str:
        pretty_list = [exp.to_dict() for exp in self.expence_list]
        return tabulate(pretty_list, headers="keys")

    def total_expence(self) -> float:
        total: float = sum([exp.amount for exp in self.expence_list])
        return total

    def total_by_month(self, month: int) -> float:
        expence: Expence
        sum: float = 0
        for expence in self.expence_list:
            exp_mounth = datetime.fromtimestamp(expence.timestamp).month
            if exp_mounth == month:
                sum += expence.amount
        return sum

    def update(self,
               id: int,
               desc: str | None,
               amount: float | None,
               category: Category | None) -> None:
        exp: Expence
        for exp in self.expence_list:
            if exp.id == id:
                exp.description = desc if desc else exp.description
                exp.amount = amount if amount else exp.amount
                exp.category = category if category else exp.category
        self.write_file()

    def read_file(self) -> None:
        try:
            with open(self.expence_file) as expence_file:
                data = json.load(expence_file)
                self.expence_list = self._format_file(data)

        except FileNotFoundError:
            print("File no found")
            self._create_file(self.expence_file)

    def _create_file(self, filepath) -> None:
        folder = os.path.normpath(os.path.join(filepath, '..'))
        if not os.path.isdir(folder):
            os.mkdir(folder)
        with open(filepath, "w") as file:
            file.write("[]")

    def _format_file(self, data: list[dict[str, Any]]):
        result = []
        for expence in data:
            category = expence['category']
            try:
                expence['category'] = Categories(
                    Category(
                        category['name'],
                        category['emoji'],
                        Group(category['group'])
                        )
                    ).value
            except ValueError:
                print('expence is corrupted')
                continue
            del expence['id']
            result.append(Expence(**expence))
        return result
