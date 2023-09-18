import uvicorn
from pydantic import BaseModel
from typing import Annotated
from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

users = []


class UserIn(BaseModel):
    name: str
    email: str
    password: str


class UserOut(BaseModel):
    id: int
    name: str
    email: str


class User(UserIn):
    id: int


@app.get("/users/", response_class=HTMLResponse)
async def get_users(request: Request):
    context = {"title": "Пользователи"}
    return templates.TemplateResponse('users.html', {'request': request, 'users': users, **context})


@app.post("/users/", response_model=UserOut)
async def add_user(user_in: UserIn):
    new_user_id = users[-1].id + 1 if len(users) else 1
    user = User(id=new_user_id, name=user_in.name, email=user_in.email, password=user_in.password)
    users.append(user)
    return UserOut(id=user.id, name=user.name, email=user.email)


@app.put("/users/", response_model=UserOut)
async def edit_user(user_id: int, user_in: UserIn):
    for user in users:
        if user.id == user_id:
            user.name = user_in.name
            user.email = user_in.email
            user.password = user_in.password
            return UserOut(id=user.id, name=user.name, email=user.email)
    raise HTTPException(status_code=404, detail='Пользователь не найден!')


@app.delete("/users/", response_model=dict)
async def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return {'message': 'Пользователь успешно удален!'}
    raise HTTPException(status_code=404, detail='Пользователь не найден!')


@app.get("/add_user/", response_class=HTMLResponse)
async def new_user(request: Request):
    context = {"title": "Добавление пользователя"}
    return templates.TemplateResponse('add_user.html', {'request': request, **context})


@app.post("/add_user/", response_class=HTMLResponse)
async def create_user(request: Request,
                      user_name: Annotated[str, Form()],
                      user_email: Annotated[str, Form()],
                      user_password: Annotated[str, Form()]):
    await add_user(UserIn(name=user_name, email=user_email, password=user_password))
    return await get_users(request)


if __name__ == '__main__':
    uvicorn.run("app_5:app", host="127.0.0.1", port=8000, reload=True)
