"""aplicación principal (modelo)"""

import os

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, DateTime

from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

from sqlalchemy.ext.declarative import declarative_base

PYTHON_ENV = os.getenv('PYTHON_ENV')

if PYTHON_ENV == 'DEV':
    engine = create_engine('sqlite:///data//mypythofolio_dev.db', echo=True)
elif PYTHON_ENV == 'PROD':
    engine = create_engine('sqlite:///data//mypythofolio.db')
else: # TEST
    engine = create_engine('sqlite:///:memory:')

class PersistentObject:
    """objeto persistente base"""
    object_id = Column('object_id', Integer, primary_key=True, nullable=False)
    timestamp = Column('timestamp', DateTime, server_default=func.now(), nullable=False)

Base = declarative_base(cls=PersistentObject)

Session = sessionmaker(bind=engine)
