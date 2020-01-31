import unittest

class TestPension(unittest.TestCase):
    def test_CreaPersona(self):
        persona = Persona()
        self.assertEqual(persona,persona)