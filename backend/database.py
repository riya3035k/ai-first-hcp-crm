import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
load_dotenv()
from sqlalchemy.engine import URL
DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password=os.getenv("DB_PASSWORD"),
    host="localhost",
    port=3306,
    database="hcp_crm"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
