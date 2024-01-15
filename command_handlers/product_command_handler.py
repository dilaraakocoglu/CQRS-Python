import dataclasses
from diator.requests import Request, RequestHandler
from diator.response import Response
from diator.events import Event, EventEmitter, EventMap
from fastapi import Depends
from db.write_db import get_write_db
from service.crud import create_product
from db.models import Product
from sqlalchemy.orm import Session

@dataclasses.dataclass(frozen=True, kw_only=True)
class CreateProductCommand(Request):
    name: str 
    description: str

@dataclasses.dataclass(frozen=True, kw_only=True)
class ProductCreatedEvent(Event):
    product_id: int


class CreateProductCommandHandler(RequestHandler[CreateProductCommand, None]):
    def __init__(self) -> None:
        self._events: list[Event] = []

    
    @property
    def events(self) -> list[Event]:
        return self._events
    
    async def handle(self, request: CreateProductCommand) -> None:
        product = create_product(request.name, request.description)
        self._events.append(ProductCreatedEvent(product_id=product.id))


