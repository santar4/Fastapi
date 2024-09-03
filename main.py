from http.client import HTTPException

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/")
def hello(name: str = Query(None, description="Введіть ваше ім'я")):
    if name:
        return {"message": f"Вітаємо, {name}!"}
    return {"message": "Вітаємо!"}


@app.get("/kalkulator")
def calkulator(operation: str, num1: float, num2: float):
    if operation == "+":
        result = num1 + num2

    elif operation == "-":
        result = num1 - num2

    elif operation == "*":
        result = num1 * num2

    elif operation == "/":
        if num1 == 0 or num2 == 0:
            raise HTTPException(status_code=400,
                                detail="Ділення на нуль не дозволено")
        result = num1 / num2

    elif operation == "%":
        if num1 == 0 or num2 == 0:
            raise HTTPException(status_code=400,
                                detail="Знайти процент від нуля неможливо")
        result = num1 % num2

    else:
        raise HTTPException(status_code=400,
                            detail="Операція є невірною,спробуйте +, -, *, /, %..")

    return {"result": result}
