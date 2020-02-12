from app import Base

from sqlalchemy import Column, String

class Broker(Base):
    __tablename__ = 'brokers'

    codigo = Column('codigo', String(10), unique=True, index=True, nullable=False)
    descripcion = Column('descripcion', String(100), nullable=False)

# 
# IOL	Invertir OnLine
# RIG	Rig Valores
# PPI	Portfolio Personal Inversiones
# BLZ	Balanz Capital
# HSBC	HSBC