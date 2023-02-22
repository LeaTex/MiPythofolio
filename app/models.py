"""objetos persistentes básicos del sistema"""

from sqlalchemy import Column, String, Integer, Enum
from sqlalchemy.sql.schema import ForeignKey

from sqlalchemy.orm import relationship, backref

from .hardcoded import TipoActivo

from . import Base, engine

class Entidad(Base):
    """Broker, Banco o entidad"""
    __tablename__ = 'entidades'

    codigo = Column('codigo', String(10), unique=True, index=True, nullable=False)
    descripcion = Column('descripcion', String(100), nullable=False)
    numero_depositante = Column('numero_depositante', Integer, nullable=True)

    def __str__(self):
        return self.codigo


class Titulo(Base):
    """Activo operable (título)"""
    __tablename__ = 'titulos'

    codigo = Column('codigo', String(10), index=True, unique=True, nullable=False)
    descripcion = Column('descripcion', String(100), nullable=False)
    nombre_corto = Column('nombre_corto', String(50))
    tipo = Column('tipo', Enum(TipoActivo, values_callable=lambda x: [str(member.value) for member in TipoActivo]), nullable=False)
    moneda_codigo = Column('moneda', String(10), ForeignKey('titulos.codigo'))
    moneda = relationship('Titulo', remote_side=[codigo], uselist=False)
    codigo_cv = Column('codigo_cv', String(10))
    codigo_isin = Column('codigo_isin', String(10))

    def __str__(self):
        return self.codigo

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.tipo.name} {self.codigo}>"


Base.metadata.create_all(bind=engine)
