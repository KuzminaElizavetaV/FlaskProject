import databases
import sqlalchemy
from settings import settings

DATABASE_URL = settings.DATABASE_URL
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(30), nullable=False),
    sqlalchemy.Column("surname", sqlalchemy.String(30), nullable=False),
    sqlalchemy.Column("email", sqlalchemy.String(30), unique=True, nullable=False),
    sqlalchemy.Column("password", sqlalchemy.String(20), nullable=False),
)

products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(50), unique=True, nullable=False),
    sqlalchemy.Column("description", sqlalchemy.String(300), nullable=True),
    sqlalchemy.Column("price", sqlalchemy.Float, nullable=False),
)

orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("users.id"), nullable=False),
    sqlalchemy.Column("product_id", sqlalchemy.ForeignKey("products.id"), nullable=False),
    sqlalchemy.Column("creation_date", sqlalchemy.Date, nullable=False),
    sqlalchemy.Column("status", sqlalchemy.String(20), nullable=False),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
