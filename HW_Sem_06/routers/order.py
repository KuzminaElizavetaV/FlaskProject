from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from HW_Sem_06.db import orders, products, users, database
from HW_Sem_06.models.order import Order, OrderIn

router = APIRouter()


@router.get("/orders/", response_model=list[Order])
async def get_orders():
    query = select(orders.c.id.label('order_id'), orders.c.creation_date.label('creation_date'),
                   orders.c.status.label('status'),
                   users.c.id.label('user_id'), users.c.name.label('user_name'),
                   users.c.surname.label('user_surname'), users.c.email.label('user_email'),
                   products.c.id.label('product_id'), products.c.title.label('product_title'),
                   products.c.description.label('product_description'), products.c.price.label('product_price')
                   ).join(products).join(users)
    return await database.fetch_all(query)


@router.get("/orders/{order_id}", response_model=Order)
async def get_order(order_id: int):
    query = select(orders.c.id.label('order_id'), orders.c.creation_date.label('creation_date'),
                   orders.c.status.label('status'),
                   users.c.id.label('user_id'), users.c.name.label('user_name'),
                   users.c.surname.label('user_surname'), users.c.email.label('user_email'),
                   products.c.id.label('product_id'), products.c.title.label('product_title'),
                   products.c.description.label('product_description'), products.c.price.label('product_price')
                   ).where(orders.c.id == order_id).join(products).join(users)
    fetch = await database.fetch_one(query)
    if not fetch:
        raise HTTPException(status_code=404, detail='Заказ не найден!')
    return fetch


@router.post("/orders/", response_model=Order)
async def add_order(order: OrderIn):
    query = orders.insert().values(user_id=order.user_id,
                                   product_id=order.product_id,
                                   creation_date=order.creation_date,
                                   status=order.status)
    last_record_id = await database.execute(query)
    return await get_order(last_record_id)


@router.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, new_order: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.model_dump())
    fetch = await database.execute(query)
    if not fetch:
        raise HTTPException(status_code=404, detail='Заказ не найден!')
    return await get_order(order_id)


@router.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    fetch = await database.execute(query)
    if not fetch:
        raise HTTPException(status_code=404, detail='Заказ не найден!')
    return {'Сообщение': 'Заказ удален!'}
