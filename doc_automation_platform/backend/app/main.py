from fastapi import FastAPI
from app.api import users
from app.api import auth

app = FastAPI(
    title="Developer Platform API",
    description="A demonstration of auto-generated documentation via FastAPI and mkdocstrings.",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def read_root() -> dict:
    """
    Root endpoint for the Developer Platform API.
    
    Returns:
        dict: A simple welcome message and API status.
    """
    return {"message": "Welcome to the Developer Platform API. Visit /docs for OpenAPI documentation."}
