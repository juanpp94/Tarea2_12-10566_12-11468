import unittest
from Persona import Persona
from datetime import date
from datetime import datetime

class TestPension(unittest.TestCase):

    #SetUp para crear una instancia de persona y no repetir codigo (refactoring)
    def crearPersona(self):
        self.p = Persona()
        self.persona = Persona()

    #Caso de Prueba para crear una instancia de la clase Persona
    def test_CrearPersona(self):
        self.assertIsInstance(self.persona,Persona)

    #Caso de Prueba para ver si una persona generica tiene pension
    def test_PensionVejezPersonaGenerica(self):
        self.p.tieneDerechoPension()

    #Caso de Prueba para verificar si un hombre de 70 anos y 750 semanas
    #rotacion tiene pension
    def test_PensionHombre70Anos750SemanasRotacion(self):
        self.p.setEdad(70)
        self.p.setSemanasRotacion(750)
        self.p.tieneDerechoPension()
        self.p.setGenero("Hombre")
        self.p.tieneDerechoPension()


    #Caso de Prueba para verificar si un Hombre de 70 anos y 749 semanas
    #rotacion tiene pension
    def test_PensionHombre70Anos749SemanasRotacion(self):
        self.p.setEdad(70)
        self.p.setSemanasRotacion(749)
        self.p.tieneDerechoPension()
        self.p.setGenero("Hombre")
        self.p.tieneDerechoPension()
    
    #Hallar la edad minima para que una persona reciba pension
    #Prueba para hombre y mujer
    def test_EdadMinimaParPensionPersonaGenerica(self):

        self.p.setGenero("Hombre")
        self.persona.setGenero("Mujer")

        edadH = self.p.edadMinimaParaOptarPorPension(self.p.genero)
        self.assertIsInstance(edadH,int)

        edadM = self.persona.edadMinimaParaOptarPorPension(self.persona.genero)
        self.assertIsInstance(edadM,int)
    
    #Caso de Prueba para verificar si una persona puede recibir pension a partir
    # de su fecha de nacimiento
    def test_PensionPersonaSegunFechaNacimiento(self):
        self.p.setGenero("Hombre")
        fecha = datetime(1994, 11, 22, 10, 15, 00, 00000)
        self.p.setFechaNacimiento(fecha)
        self.persona.setGenero("Mujer")
        self.persona.setFechaNacimiento(fecha)

    #Caso de Prueba para verificar si una persona tiene la edad minima para
    #optar por la pension
    def test_PersonaTieneEdadMinimaParaOptarPension(self):
        self.p.setGenero = "Hombre"
        fechaNacimientoH = date(1994,11,22,10,15,00)
        fechaActual = datetime.now()
        edadH = fechaActual - fechaNacimientoH
        self.p.edad = edadH

        self.p.tieneEdadParaOptarPension(self.p.genero,self.p.edad)

        self.persona.setGenero = "Mujer"
        fechaNacimientoM = date(1995,11,22,10,15,00)
        fechaActual = datetime.now()
        edadM = fechaActual - fechaNacimientoM
        self.persona.edad = edadM
        puedeOptar = self.persona.tieneEdadParaOptarPension(self.persona.genero,self.persona.edad)

    #Caso de Prueba: Verifica si una persona tiene la cantidad de semanas de rotacion
    #y la edad minima para cobrar pension
        self.p.setGenero = "Hombre"
        fechaNacimientoH = date(1960,12,6,10,15,00)
        fechaActual = datetime.now()
        edadH = fechaActual - fechaNacimientoH
        self.p.edad = edadH

        puedeOptar = self.persona.tieneDerechoPension()
        self.assertTrue(puedeOptar)
        
