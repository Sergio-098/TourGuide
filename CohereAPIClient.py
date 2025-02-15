import cohere

class CohereApiClient:
    def __init__(self, api_key: str):
        self.co = cohere.Client(api_key)

    def generate_itinerary(self, place: str, emphasis: List[str], days: int, max_price: float) -> str:
        emphasis_str = ", ".join(emphasis)  # Convert list to readable string

        prompt = f"""
        You are a travel planner AI. Generate a detailed {days}-day itinerary for {place}
        with an absolute maximum estimated cost of {max_price} CAD (excluding flights/accommodation).
        The traveler is interested in {emphasis_str} experiences.
        
        Each day should include:
        - Morning activity
        - Lunch recommendation
        - Afternoon activity
        - Dinner recommendation
        - Evening activity (optional)
        
        Format the response strictly as:
        
        Day 1:
        Estimated Price For all the Day's Activities in CAD as a singular float number
        - Morning: ...
        - Lunch: ...
        - Afternoon: ...
        - Dinner: ...
        - Evening: ...
        
        Do NOT include extra text before or after the itinerary.
        """

        response = self.co.generate(
            model="command-r",
            prompt=prompt,
            max_tokens=500
        )

        return response.generations[0].text
