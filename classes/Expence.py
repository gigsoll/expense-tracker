from dataclasses import dataclass
from datetime import datetime
from classes.Category import Group, Category


@dataclass
class Expence:
    description: str
    amount: float
    category: Category = Category("other", "💡", Group.OTHER)
    date: str = datetime.strftime(datetime.today(), "%Y-%m-%d")
    time: str = datetime.strftime(datetime.now(), "%H:%M:%S")
