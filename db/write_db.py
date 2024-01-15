from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

write_database_url = "postgresql://postgres:1234@localhost:5432"
write_engine = create_engine(write_database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=write_engine)

def init_db():
    Base.metadata.create_all(bind=write_engine)

def get_write_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()