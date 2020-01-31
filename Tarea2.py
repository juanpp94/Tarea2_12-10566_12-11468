import unittest
from Persona import Persona
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


