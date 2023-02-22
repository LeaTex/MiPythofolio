"""objetos hardcodeados"""

from enum import Enum, unique

@unique
class TipoEvento(Enum):
    """Tipo de evento"""
    INGRESO = 'I'
    EGRESO = 'E'


@unique
class ConceptoEvento(Enum):
    """Concepto de evento"""
    RENTA = 'RTA'
    OPERACION = 'OPE'
    IVA = 'IVA'
    IMPUESTO = 'IMP'
    DIVIDENDO = 'DIV'
    DERECHO_MERCADO = 'DER'
    COMISION = 'COM'
    AMORTIZACION = 'AMO'


@unique
class TipoActivo(Enum):
    """Tipo de activo"""
    ACCION = 'ACC'
    BONO_NACIONAL = 'BON'
    BONO_PROVINCIAL = 'BOP'
    CEDEAR = 'CED'
    CUOTAPARTE = 'CP'
    LEBAC = 'LEB'
    LETE = 'LET'
    MONEDA = 'MON'
    OBLIGACION_NEGOCIABLE = 'ON'
    OTRO = 'OTR'
