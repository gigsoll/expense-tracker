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
    timestamp: float = datetime.now().timestamp()

    def to_dict(self) -> dict[str, Any]:
        time = datetime.fromtimestamp(self.timestamp)
        return {
            "ID": self.id,
            "Description": self.description,
            "Amount": self.amount,
            "Category": f"{self.category.emoji} {self.category.name}",
            "date": datetime.strftime(time, "%Y-%m-%d"),
            "time": datetime.strftime(time, "%H:%M:%S")
        }
