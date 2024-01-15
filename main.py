from fastapi import FastAPI
from api.endpoints import router as api_router
from db.read_db import init_db as read_init_db
from db.write_db import init_db as write_init_db
from command_handlers.product_command_handler import CreateProductCommandHandler, CreateProductCommand

app = FastAPI()

app.include_router(api_router)

read_init_db()
write_init_db()
