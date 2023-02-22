"""operaciones"""

from sqlalchemy import Column, String, Integer, Numeric, Enum, Date
from sqlalchemy.sql.schema import ForeignKey

from sqlalchemy.orm import relationship, backref

from .hardcoded import ConceptoEvento, TipoEvento
from .models import Titulo, Entidad

from . import Base, engine

# class Evento(Base):
#     """evento de ingreso o egreso de moneda o especie"""
#     __tablename__ = 'eventos'

#     fecha_concertacion = Column('fecha_concertacion', Date, nullable=False)
#     fecha_liquidacion = Column('fecha_liquidacion', Date, nullable=False)
#     tipo = Column('tipo', Enum(TipoEvento, values_callable=lambda x: [str(member.value) for member in TipoEvento]), nullable=False)
#     concepto  = Column('concepto', Enum(ConceptoEvento, values_callable=lambda x: [str(member.value) for member in ConceptoEvento]), nullable=False)

#     cantidad = Column('cantidad', Numeric(12,2), nullable=False)
    
#     moneda_codigo = Column('moneda', String(10), ForeignKey('monedas.codigo'))

class CaucionColocadora(Base):
    """caución colocadora"""
    __tablename__ = 'cauciones_colocadoras'

    entidad_codigo = Column('entidad', String(10), ForeignKey('entidades.codigo'), nullable=False)
    entidad = relationship('Entidad', lazy='joined', uselist=False)
    fecha_concertacion = Column('fecha_concertacion', Date, nullable=False)
    cantidad = Column('cantidad', Numeric(12, 2, asdecimal=False), nullable=False)
    moneda_codigo = Column('moneda', String(10), ForeignKey('titulos.codigo'), nullable=False)
    moneda = relationship('Titulo', lazy='joined', primaryjoin=lambda: CaucionColocadora.moneda_codigo == Titulo.codigo, uselist=False)
    plazo_dias = Column('plazo_dias', Integer, nullable=False)
    tasa_tna = Column('tasa_tna', Numeric(7, 3, asdecimal=False), nullable=False)
    fecha_liquidacion = Column('fecha_liquidacion', Date, nullable=False)
    bruto = Column('bruto', Numeric(12, 2, asdecimal=False), nullable=False)
    arancel = Column('arancel', Numeric(12, 2, asdecimal=False), nullable=False)
    derecho_mercado = Column('derecho_mercado', Numeric(12, 2, asdecimal=False), nullable=False)
    iva = Column('iva', Numeric(12, 2, asdecimal=False), nullable=False)
    moneda_gastos_codigo = Column('moneda_gastos', String(10), ForeignKey('titulos.codigo'), nullable=False)
    moneda_gastos = relationship('Titulo', lazy='joined', primaryjoin=lambda: CaucionColocadora.moneda_gastos_codigo == Titulo.codigo, uselist=False)
    tipo_cambio = Column('tipo_cambio', Numeric(12,2, asdecimal=False), nullable=False, default=1.0)

    def interes(self):
        return self.bruto - self.cantidad

    def neto(self):
        return self.bruto - self.arancel - self.derecho_mercado - self.iva # TODO: ojo con TC

    def ganancia(self):
        return self.neto() - self.cantidad


class PlazoFijo(Base):
    """plazo fijo"""
    __tablename__ = 'plazos_fijos'

    entidad_codigo = Column('entidad', String(10), ForeignKey('entidades.codigo'), nullable=False)
    entidad = relationship('Entidad', lazy='joined', uselist=False)
    fecha_concertacion = Column('fecha_concertacion', Date, nullable=False)
    cantidad = Column('cantidad', Numeric(12, 2, asdecimal=False), nullable=False)
    moneda_codigo = Column('moneda', String(10), ForeignKey('titulos.codigo'), nullable=False)
    moneda = relationship('Titulo', lazy='joined', uselist=False)
    plazo_dias = Column('plazo_dias', Integer, nullable=False)
    tasa_tna = Column('tasa_tna', Numeric(7, 3, asdecimal=False), nullable=False)
    fecha_vencimiento = Column('fecha_vencimiento', Date, nullable=False)
    bruto = Column('bruto', Numeric(12, 2, asdecimal=False), nullable=False)

    def interes(self):
        return self.bruto - self.cantidad

Base.metadata.create_all(bind=engine)
