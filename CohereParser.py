import re

from Day import Day
from Trip import Trip


class CohereParser:
    @staticmethod
    def parse_itinerary(response_text: str) -> Trip:
        days = []
        day_blocks = response_text.split("Day ")

        for day_block in day_blocks[1:]:  # Ignore the first split (empty)
            lines = day_block.strip().split("\n")
            activities = {}
            estimated_price = float(lines[1])

            for line in lines[2:]:  # Skip "Day X:" line
                match = re.match(r"- (\w+): (.+)", line)
                if match:
                    activities[match.group(1)] = match.group(2)

            days.append(Day(activities=activities, estimated_price=estimated_price))

        return Trip(num_days=len(days), days=days, place="Unknown", emphasis=[])
