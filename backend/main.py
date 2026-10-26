from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    """
    Root endpoint that returns a welcome message.
    FastAPI Docs: https://fastapi.tiangolo.com/tutorial/first-steps/
    """
    return {"message": "Hello World"}