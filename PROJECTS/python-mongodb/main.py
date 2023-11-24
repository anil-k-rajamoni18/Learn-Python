from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# get endpoint
@app.get("/api/greet")
async def greet() -> str:
    return f'Hello Welcome to fast api session'


# endpoint with path variable
@app.get("/api/greet/{name}")
async def greet_user(name: str) -> dict:
    return {"message": f"Hello {name}"}


# query params
@app.get("/api/add")
async def addition(num1: int, num2: int) -> dict:
    return {"addition": num1 + num2}
