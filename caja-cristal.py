import imp
from pickletools import read_uint1


import unittest

def esMayorDeEdad(edad):
    if edad >= 18:
        return True
    else:
        return False

class PruebaDeCristalTest(unittest.TestCase):
    def test_mayor_de_edad(self):
        edad = int(input('Dame tu edad (solo escribe el número entero):'))
        resultado = esMayorDeEdad(edad)
        self.assertEqual(resultado, True)


if __name__=='__main__':
    unittest.main()