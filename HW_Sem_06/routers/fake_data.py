import datetime
from random import randint, choice
from fastapi import APIRouter
from HW_Sem_06.db import orders, products, users, database

router = APIRouter()


@router.get("/fake_data/")
async def create_fake_data(num_users: int, num_products: int, num_orders: int):
    for i in range(num_users):
        query = users.insert().values(name=f'Name_{i}',
                                      surname=f'Surname_{i}',
                                      email=f'user{i}@ya.ru',
                                      password=f'password_{i}')
        await database.execute(query)

    for i in range(num_products):
        query = products.insert().values(title=f'item_{i}',
                                         description=f'description_{i}',
                                         price=randint(1000, 99999) / 100)
        await database.execute(query)

    for i in range(num_orders):
        query = orders.insert().values(user_id=randint(1, num_users),
                                       product_id=randint(1, num_products),
                                       creation_date=datetime.date.today(),
                                       status=choice(['В сборке', 'Передается в доставку', 'В пути',
                                                      'Ожидает получения', 'Получен', 'Отменён']))
        await database.execute(query)

    return {'Сообщение': f'Было создано {num_users} пользователей, {num_products} товаров и {num_orders} заказов'}
