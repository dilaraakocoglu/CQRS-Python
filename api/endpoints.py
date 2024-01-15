from fastapi import APIRouter, HTTPException, Query, Depends
from command_handlers.product_command_handler import CreateProductCommandHandler, CreateProductCommand
from query_handlers.product_query_handler import ListProductsQueryHandler, ListProductsQuery
from db.models import Product
from di import Container, bind_by_type
from di.dependent import Dependent
from diator.container.di import DIContainer
from diator.events import Event, EventEmitter, EventMap
from diator.mediator import Mediator
from diator.requests import Request, RequestHandler, RequestMap
from sqlalchemy.orm import Session

router = APIRouter()


def setup_di() -> DIContainer:
    external_container = Container()

    external_container.bind(
        bind_by_type(
            Dependent(CreateProductCommandHandler, scope="request"),
            CreateProductCommandHandler,
        )
    )
    container = DIContainer()
    container.attach_external_container(external_container)

    return container

container = setup_di()

request_map = RequestMap()
request_map.bind(CreateProductCommand, CreateProductCommandHandler)
request_map.bind(ListProductsQuery, ListProductsQueryHandler)

event_emitter = EventEmitter(event_map=EventMap(), container=container, message_broker=None)

mediator = Mediator(
    request_map=request_map,
    event_emitter=event_emitter,
    container=container,
)

@router.post("/products/")
async def create_product(name: str, description: str):
    command = CreateProductCommand(name=name, description=description)
    product = await mediator.send(command)
    return product

@router.get("/products/")
async def get_products():
    query = ListProductsQuery()
    products = await mediator.send(query)
    return products
