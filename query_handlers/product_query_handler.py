from fastapi import Depends
from db.read_db import get_read_db
from service.crud import get_products
from diator.requests import Request, RequestHandler
from diator.response import Response
from diator.events import Event, EventEmitter, EventMap
from sqlalchemy.orm import Session

class ListProductsQuery(Request):
    pass

class ListProductsQueryHandler(RequestHandler[ListProductsQuery, list]):
    def __init__(self) -> None:
        pass
    async def handle(self, request: ListProductsQuery) -> list:
        products = get_products()
        return products