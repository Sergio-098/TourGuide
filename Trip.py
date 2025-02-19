from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

class Day(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    trip_id: int = Field(foreign_key="trip.id")
    morning: str
    lunch: str
    afternoon: str
    dinner: str
    evening: str
    price: float

    def edit_day(self, activity : str, new_price: int, old_price: int, new_act: str):
        self.activities[activity] = new_act
        self.price += (new_price - old_price)


class Trip(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    place: str
    vibe: str
    num_days: int
    price: float
    days: List[Day] = Relationship(back_populates="trip")

    def __post_init__(self):
        self.price = self.calculate_total_price()

    def calculate_total_price(self) -> float:
        return sum(day.estimated_price for day in self.days)

    def edit_price(self, new_price: float):
        self.price += new_price


Day.trip = Relationship(back_populates="days")
