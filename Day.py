from typing import Dict
from dataclasses import dataclass

@dataclass
class Day:
    activities: Dict[str, str]  # Keys: "Morning", "Lunch", "Afternoon", "Dinner", "Evening"
    estimated_price: float      # Cost estimate for the day's activities

    def edit_day(self, activity : str, new_price: int, old_price: int, new_act: str):
        self.activities[activity] = new_act
        self.estimated_price += (new_price - old_price)

