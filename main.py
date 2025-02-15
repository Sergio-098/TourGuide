from fastapi import FastAPI
import cohere

app = FastAPI()
co = cohere.Client("CuWbbgwC7Sy8XKJKMn53bPmjcerPmf12uFnQ4klu")

@app.get("/")
def home():
    return {"message": "Trip Planner API is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
