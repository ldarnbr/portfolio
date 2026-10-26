from fastapi import FastAPI
from typing import List
import schemas

app = FastAPI()

@app.get("/")
async def root():
    """
    Root endpoint that returns a welcome message.
    FastAPI Docs: https://fastapi.tiangolo.com/tutorial/first-steps/
    """
    return {"message": "Hello World"}

@app.get("/projects", response_model=List[schemas.Project])
async def get_projects():
    """
    Returns a list of portfolio projects.
    """
    return [
        {"id": 1, "title": "Portfolio Website", "tech": ["React", "FastAPI", "TypeScript", "Python"]},
        {"id": 2, "title": "Portfolio Website", "tech": ["Example1", "Example2", "Example3"]}
    ]