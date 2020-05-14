from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Numeric, String, MetaData, ForeignKey

db = create_engine('sqlite:///store.db', echo = True)
session = sessionmaker(bind=db)
Base = declarative_base()

def ses():
    return session()


