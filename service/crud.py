from sqlalchemy.orm import Session
from db.models import Product
from db.read_db import get_read_db
from db.write_db import get_write_db

w_db = next(get_write_db())
r_db = next(get_read_db())

def create_product(name: str, description: str):
    db_product = Product(name=name, description=description)
    w_db.add(db_product)
    w_db.commit()
    w_db.refresh(db_product)
    return db_product

def get_products():
    return r_db.query(Product).all()