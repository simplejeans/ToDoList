from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_NAME = "todo.db"
engine = create_engine(f"sqlite:///{DATABASE_NAME}?check_same_thread=False")

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


def create_database():
    Base.metadata.create_all(engine)
