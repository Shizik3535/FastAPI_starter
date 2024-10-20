from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Starter",
    version="0.1.0",
    description="FastAPI Starter for async API",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
