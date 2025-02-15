from typing import List
from dataclasses import dataclass, field
from Day import Day

@dataclass
class Trip:
    num_days: int
    days: List[Day]
    place: str
    emphasis: List[str]  # Store as a list instead of comma-separated string
    price: float = field(init=False)  # Auto-calculated in `__post_init__`

    def __post_init__(self):
        self.price = self.calculate_total_price()

    def calculate_total_price(self) -> float:
        return sum(day.estimated_price for day in self.days)

    def edit_price(self, new_price: float):
        self.price += new_price

