import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.tyyppimuunnos'

@points('2.tyyppimuunnos')
class TyyppimuunnnosTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', retun_value ='0'):
            cls.module = load_module(exercise, 'fi')

    def test_lukuja(self):
        values = "0.1 1.34 101.001 12.474747".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                intpart = value[:value.find(".")]
                decpart = "0" + value[value.find(".") :]
                reload_module(self.module)
                acual_output = get_stdout()
                output = acual_output.split("\n")
            
                self.assertTrue(len(acual_output)>0, "Ohjelmasi ei tulosta mitään syötteellä {}".format(value))
                self.assertTrue(len(output) == 2, "Ohjelmasi tulostaa kahden rivin sijasta {} riviä syötteellä {}".format(len(output), value))
                self.assertTrue(output[0].find(str(intpart)) > -1, "Tulosteesta {} ei löydy oikeaa kokonaisosaa {} syötteellä {}".format(output[0], intpart, value))
                self.assertTrue(output[1].find(str(decpart)) > -1, "Tulosteesta {} ei löydy oikeaa desimaalisosaa {} syötteellä {}".format(output[1], decpart, value))
   
if __name__ == '__main__':
    unittest.main()