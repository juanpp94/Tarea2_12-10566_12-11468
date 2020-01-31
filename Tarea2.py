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

    #Caso de Prueba para verificar si un hombre de 70 anos y 479 semanas
    #rotacion tiene pension
    def test_PensionHombre70Anos479SemanasRotacion(self):
        p = Persona()
        p.setEdad(70)
        p.setSemanasRotacion(479)
        p.tieneDerechoPension()

