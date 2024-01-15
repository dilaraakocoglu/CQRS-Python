from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

read_database_url = "postgresql://postgres:1234@localhost:5433"
read_engine = create_engine(read_database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=read_engine)

def init_db():
    Base.metadata.create_all(bind=read_engine)

def get_read_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
