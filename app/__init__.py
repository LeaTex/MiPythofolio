from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Numeric, String, DateTime, Boolean, ForeignKey

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///..//brokers.db', echo=True)

class PersistentObject(object):
    objectID = Column('object_id', Integer(), primary_key=True, nullable=False)
    timestamp = Column('timestamp', DateTime(), default=datetime.now, nullable=False)

Base = declarative_base(cls=PersistentObject)

Session = sessionmaker(bind=engine)

# Base.metadata.create_all(bind=engine)
