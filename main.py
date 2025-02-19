from fastapi import FastAPI
from database import init_db
import cohere

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

co = cohere.Client("CuWbbgwC7Sy8XKJKMn53bPmjcerPmf12uFnQ4klu")

@app.get("/")
def home():
    return {"message": "Trip Planner API is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
