from classes.Category import Category, Group
from enum import Enum


class Categories(Enum):
    SERVICE = Category("Car service", "🚗", Group.CAR)
    FUEL = Category("Car fuel", "⛽", Group.CAR)
    WATER = Category("Water bill", "💧", Group.BILLS)
    GAS = Category("Gas bill", "🔥", Group.BILLS)
    ELECTRICITY = Category("Electicity bill", "⚡", Group.BILLS)
    CINEMA = Category("Cinema", "📽️", Group.RECREATION)
    SHOPING = Category("Shiping", "🛍️", Group.RECREATION)
    RESTAURANT = Category("Restaurant", "🍽️", Group.RECREATION)
    MEDICINE = Category("Medicine", "🏥", Group.IMPORTANT)
    CLOTHES = Category("Clothes", "👚", Group.IMPORTANT)
    FOOD = Category("Food", "🍞", Group.IMPORTANT)
    SCHOOL = Category("School", "🏫", Group.IMPORTANT)
    OTHER = Category("other", "💡", Group.OTHER)
