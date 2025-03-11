from itertools import count
from typing import Any
from dataclasses import dataclass, field
from datetime import datetime
from classes.Category import Category
from classes.Categories import Categories


@dataclass
class Expence:
    description: str
    amount: float
    id: int = field(default_factory=count(1).__next__)
    category: Category = Categories.OTHER.value
    date: str = datetime.strftime(datetime.today(), "%Y-%m-%d")
    time: str = datetime.strftime(datetime.now(), "%H:%M:%S")

    def to_dict(self) -> dict[str, Any]:
        return {
            "ID": self.id,
            "Description": self.description,
            "Amount": self.amount,
            "Category": f"{self.category.emoji} {self.category.name}",
            "date": self.date,
            "time": self.time
        }
