import unittest
from Persona import Persona
class TestPension(unittest.TestCase):

    #Caso de Prueba para crear una instancia de la clase Persona
    def test_CrearPersona(self):
        persona = Persona()
        self.assertIsInstance(persona,Persona)

