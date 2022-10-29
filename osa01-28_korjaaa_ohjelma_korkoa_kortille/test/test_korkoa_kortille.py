import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.korkoa_kortille'

@points('1.korkoa_kortille')
class KorkoaKortilleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def check(self,output,pisteet,oikeat_pisteet):
        check1 = output.find(str(oikeat_pisteet)[:5]) > -1
        check2 = output.find(str(oikeat_pisteet+1e-9)[:5]) > -1
        check3 = output.find(str(oikeat_pisteet-1e-9)[:5]) > -1
        self.assertTrue(check1 or check2 or check3, "Syötteellä {} oikeaa pistemäärää {} ei löydy tulosteestasi {}".format(pisteet, oikeat_pisteet, output))

    def test_alle_99(self):
        pisteet = 99
        oikeat_pisteet = 1.1 * pisteet
        with patch('builtins.input', return_value = str(pisteet)):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            self.assertTrue(len(output_list) == 2, "Ohjelmasi tulostaa syötteellä {} kahden rivin sijasta {} riviä".format(pisteet, len(output_list)))
            self.assertTrue(output.find("Sait 10") > -1, "Tulosteesta ei löydy riviä 'Sait 10 % bonusta', tulosteesi on " + output)
            self.assertFalse(output.find("15 % bonusta") > -1, "Tulosteesta löytyy väärä bonusluku, 15 %:', tulosteesi on " + output)
            self.check(output,pisteet,oikeat_pisteet)

    def test_alle_100_satunnainen(self):
        pisteet = randint(1,90)
        oikeat_pisteet = 1.1 * pisteet
        with patch('builtins.input', return_value = str(pisteet)):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            self.assertTrue(len(output_list) == 2, "Ohjelmasi tulostaa syötteellä {} kahden rivin sijasta {} riviä".format(pisteet, len(output_list)))
            self.assertTrue(output_list[0].find("Sait 10") > -1, "Tulosteesta ei löydy riviä 'Sait 10 % bonusta', tulosteesi on " + output)
            self.assertFalse(output_list[0].find("15 % bonusta") > -1, "Tulosteesta löytyy väärä bonusluku, 15 %:', tulosteesi on " + output)        
            self.check(output,pisteet,oikeat_pisteet)

    def test_100(self):
        pisteet = 100
        oikeat_pisteet = 1.15 * pisteet
        with patch('builtins.input', return_value = str(pisteet)):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            self.assertTrue(len(output_list) == 2, "Ohjelmasi tulostaa syötteellä {} kahden rivin sijasta {} riviä".format(pisteet, len(output_list)))
            self.assertTrue(output_list[0].find("Sait 15") > -1, "Tulosteesta ei löydy riviä 'Sait 15 % bonusta', tulosteesi on " + output)
            self.assertFalse(output_list[0].find("10 % bonusta") > -1, "Tulosteesta löytyy väärä bonusluku, 10 %:', tulosteesi on " + output)        
            self.check(output,pisteet,oikeat_pisteet)

    def test_yli_100_satunnainen(self):
        pisteet = randint(101,1000)
        oikeat_pisteet = 1.15 * pisteet
        with patch('builtins.input', return_value = str(pisteet)):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            self.assertTrue(len(output_list) == 2, "Ohjelmasi tulostaa syötteellä {} kahden rivin sijasta {} riviä".format(pisteet, len(output_list)))
            self.assertTrue(output_list[0].find("Sait 15") > -1, "Tulosteesta ei löydy riviä 'Sait 15 % bonusta', tulosteesi on " + output)
            self.assertFalse(output_list[0].find("10 % bonusta") > -1, "Tulosteesta löytyy väärä bonusluku, 10 %:', tulosteesi on " + output)        
            self.check(output,pisteet,oikeat_pisteet)
   
if __name__ == '__main__':
    unittest.main()
