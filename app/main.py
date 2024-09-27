from fastapi import FastAPI
from app.api.endpoints import posts, users

app = FastAPI()
app.include_router(posts.router)
app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the 4create task project"}