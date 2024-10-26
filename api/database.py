from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE = "sqlite:///database.db"

engine = create_engine(
    DATABASE,
    connect_args={"check_same_thread": False},
    echo=True
)

MySession = sessionmaker(bind=engine)