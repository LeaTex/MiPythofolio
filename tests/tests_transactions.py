import os, sys
from pathlib import Path

os.environ['PYTHON_ENV'] = 'TEST'
sys.path.append(str(Path(__file__).parent.parent))

import unittest
from unittest import TestCase

import datetime

from app import Session

from app.hardcoded import TipoActivo
from app.models import Entidad, Titulo
from app.transactions import CaucionColocadora, PlazoFijo

active_session = Session()

iol = Entidad(codigo='IOL', descripcion='Invertir OnLine', numero_depositante=151)
active_session.add(iol)

peso = Titulo(codigo='ARS', descripcion='Peso', codigo_cv='8000', codigo_isin='ARARGE122945', tipo=TipoActivo.MONEDA)
active_session.add(peso)

dolar = Titulo(codigo='USD', descripcion='Dólar', codigo_cv='10000', tipo=TipoActivo.MONEDA)
active_session.add(dolar)

active_session.commit()

active_session.close()

class CaucionColocadoraTests(TestCase):

    def setUp(self):
        self.active_session = Session()
    
    def tearDown(self):
        self.active_session.close()

    def test_persistencia(self):

        caucion = CaucionColocadora(entidad = iol, fecha_concertacion = datetime.date(2020, 5, 17), cantidad = 1520, moneda = peso, 
                    plazo_dias = 3, tasa_tna = 60.5, fecha_liquidacion = datetime.date(2020, 5, 20), bruto = 1875.25, arancel = 1.8, 
                    derecho_mercado = 2.3, iva = 0.77, moneda_gastos = dolar)

        self.active_session.add(caucion)
        self.active_session.commit()

        caucion = self.active_session.query(CaucionColocadora).first()

        self.assertEqual(iol, caucion.entidad)
        self.assertEqual(datetime.date(2020, 5, 17), caucion.fecha_concertacion)
        self.assertEqual(1520, caucion.cantidad)
        self.assertEqual(peso, caucion.moneda)
        self.assertEqual(3, caucion.plazo_dias)
        self.assertEqual(60.5, caucion.tasa_tna)
        self.assertEqual(datetime.date(2020, 5, 20), caucion.fecha_liquidacion)
        self.assertEqual(1875.25, caucion.bruto)
        self.assertEqual(1.8, caucion.arancel)
        self.assertEqual(2.3, caucion.derecho_mercado)
        self.assertEqual(0.77, caucion.iva)
        self.assertEqual(dolar, caucion.moneda_gastos)
        self.assertEqual(1.0, caucion.tipo_cambio)

class PlazoFijoTests(TestCase):

    def setUp(self):
        self.active_session = Session()
    
    def tearDown(self):
        self.active_session.close()

    def test_persistencia(self):

        ppff = PlazoFijo(entidad = iol, fecha_concertacion = datetime.date(2020, 5, 17), cantidad = 1520, moneda = peso, 
                    plazo_dias = 31, tasa_tna = 62.75, fecha_vencimiento = datetime.date(2020, 5, 20), bruto = 1875.25)

        self.active_session.add(ppff)
        self.active_session.commit()

        ppff = self.active_session.query(PlazoFijo).first()

        self.assertEqual(iol, ppff.entidad)
        self.assertEqual(datetime.date(2020, 5, 17), ppff.fecha_concertacion)
        self.assertEqual(1520, ppff.cantidad)
        self.assertEqual(peso, ppff.moneda)
        self.assertEqual(31, ppff.plazo_dias)
        self.assertEqual(62.75, ppff.tasa_tna)
        self.assertEqual(datetime.date(2020, 5, 20), ppff.fecha_vencimiento)
        self.assertEqual(1875.25, ppff.bruto)


if __name__ == '__main__':
    unittest.main()