from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL ="postgresql://postgres:mypassword@localhost/GP-Database"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:mypassword@localhost/GP-Database"