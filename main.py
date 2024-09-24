from http.client import HTTPException

import httpx
from fastapi import FastAPI, Query, HTTPException


app = FastAPI()


@app.get("/")
def hello(name: str = Query(None, description="Введіть ваше ім'я")):
    if name:
        return {"message": f"Вітаємо, {name}!"}
    return {"message": "Вітаємо!"}


@app.get("/kalkulator")
def calkulator(operation: str, num1: float, num2: float):
    try:
        if operation == "+":
            result = num1 + num2

        elif operation == "-":
            result = num1 - num2

        elif operation == "*":
            result = num1 * num2

        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError("Ділення на нуль не дозволено")
            result = num1 / num2

        elif operation == "%":
            if num2 == 0:
                raise ZeroDivisionError("Знайти процент від нуля неможливо")

            result = (num1 / num2) * 100

        else:
            raise HTTPException(status_code=400,
                                detail="Операція є невірною, спробуйте +, -, *, /, %..")

    except ZeroDivisionError as abc:
        raise HTTPException(status_code=400, detail=abc)

    return {"result": result}



Base_url = "https://jsonplaceholder.typicode.com"
@app.get("/posts/")
async def all_posts():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{Base_url}/posts")
        return response.json()

@app.get("/users/")
async def all_users():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{Base_url}/users")
        return response.json()
@app.get("/posts/create")
async def create_post(title: str, body: str, user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{Base_url}/posts", json={
            "title": title,
            "body": body,
            "userId": user_id
        })
        return response.json()

@app.get("/posts/{post_id}")
async def update_post(post_id: int, title: str, body: str):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{Base_url}/posts/{post_id}", json={
            "title": title,
            "body": body
        })
        return response.json()
@app.delete("/posts/delete")
async def delete_post(post_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{Base_url}/posts/{post_id}")
        return response.status_code







