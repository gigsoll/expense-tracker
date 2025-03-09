from dataclasses import dataclass, field
from enum import StrEnum


class Group(StrEnum):
    CAR = "car"
    BILLS = "bills"
    RECREATION = "recreation"
    IMPORTANT = "important"
    OTHER = "other"


@dataclass(frozen=True)
class Category:
    name: str
    emoji: str
    group: Group = field()
