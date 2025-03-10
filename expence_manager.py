import os
import json
from dataclasses import asdict
from classes.Expence import Expence
from platformdirs import user_cache_dir
from classes.Categories import Categories
from classes.Category import Category, Group


class ExepnceManager():
    def __init__(self):
        self.expence_list: list[Expence] = []
        self.cahcedir = user_cache_dir("expence_tracker", "gigsoll")
        self.expence_file = os.path.join(self.cahcedir, "expences.json")

    def write_file(self):
        data = json.dumps(
            [asdict(exp) for exp in self.expence_list],
            indent=4
        )
        with open(self.expence_file, "w") as expence_file:
            expence_file.write(data)

    def add(self, expence: Expence) -> None:
        self.expence_list.append(expence)

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

    def _format_file(self, data):
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


def main():
    em = ExepnceManager()
    em.read_file()
    em.add(Expence("new", 200))
    em.write_file()


if __name__ == "__main__":
    main()
