from app import Base

from sqlalchemy import Column, String

class TipoActivo(Base):
    __tablename__ = 'tipos_de_activos'

    codigo = Column('codigo', String(10), unique=True, index=True, nullable=False)
    descripcion = Column('descripcion', String(100), nullable=False)

# 
# ACC	Acción
# BON	Bono Nacional
# CP	Cuotaparte
# CED	Cedear
# ON	Obligación Negociable
# BOP	Bono Provincial
# LEB	Lebac
# LET	Lete
# MON	Moneda