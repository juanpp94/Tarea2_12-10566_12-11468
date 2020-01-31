import unittest
from Persona import Persona
class TestPension(unittest.TestCase):

    #Caso de Prueba para crear una instancia de la clase Persona
    def test_CrearPersona(self):
        persona = Persona()
        self.assertIsInstance(persona,Persona)

    #Caso de Prueba para ver si una persona generica tiene pension
    def test_PensionVejezPersonaGenerica(self):
        p = Persona()
        p.tieneDerechoPension()

