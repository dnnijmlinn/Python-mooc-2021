import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.palkka'

@points('1.palkka')
class PalkkaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0","0",""]):
            cls.module = load_module(exercise, 'fi')

    def test_muut_paivat_1(self):
        hours = randint(5,15)
        perhour = float(randint(10,25))
        test_input = "{},{},tiistai".format(perhour, hours)
        ilist = test_input.split(",")
        with patch('builtins.input', side_effect=ilist):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            self.assertTrue(len(output_list) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä".format(len(output_list)))
            self.assertTrue(output.find(str(hours * perhour)) > -1, "Syötteellä {} oikeaa palkkaa {} ei löydy tulosteestasi {}".format(test_input, (hours * perhour), output))
            oikea = "Palkka {} euroa".format((hours * perhour))
            self.assertEqual(output, oikea, "Tulostus on väärässä muodossa, oikea tulostus on\n{}\nmutta ohjelmasi tulostaa\n{}".format(oikea,output))
    
    def test_muut_paivat_2(self):
        hours = randint(5,15)
        perhour = float(randint(20,35))
        test_input = "{},{},tiistai".format(perhour, hours)
        ilist = test_input.split(",")
        with patch('builtins.input', side_effect=ilist):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            self.assertTrue(len(output_list) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä".format(len(output_list)))
            self.assertTrue(output.find(str(hours * perhour)) > -1, "Syötteellä {} oikeaa palkkaa {} ei löydy tulosteestasi {}".format(test_input, (hours * perhour), output))
            oikea = "Palkka {} euroa".format((hours * perhour))
            self.assertEqual(output, oikea, "Tulostus on väärässä muodossa, oikea tulostus on\n{}\nmutta ohjelmasi tulostaa\n{}".format(oikea,output))
    
    def test_sunnuntai_1(self):
        hours = randint(5,15)
        perhour = float(randint(10,25))
        test_input = "{},{},sunnuntai".format(perhour, hours)
        ilist = test_input.split(",")
        with patch('builtins.input', side_effect=ilist):
            reload_module(self.module)
            output = get_stdout()
            perhour *= 2
            output_list = output.split("\n")
            self.assertTrue(len(output_list) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä".format(len(output_list)))
            self.assertTrue(output.find(str(hours * perhour)) > -1, "Syötteellä {} oikeaa palkkaa {} ei löydy tulosteestasi {}".format(test_input, (hours * perhour), output))
            oikea = "Palkka {} euroa".format((hours * perhour))
            self.assertEqual(output, oikea, "Tulostus on väärässä muodossa, oikea tulostus on\n{}\nmutta ohjelmasi tulostaa\n{}".format(oikea,output))
    
    def test_sunnuntai_2(self):
        hours = randint(5,15)
        perhour = float(randint(10, 25))
        test_input = "{},{},sunnuntai".format(perhour, hours)
        ilist = test_input.split(",")
        with patch('builtins.input', side_effect=ilist):
            reload_module(self.module)
            output = get_stdout()
            perhour *= 2
            output_list = output.split("\n")
            self.assertTrue(len(output_list) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä".format(len(output_list)))
            self.assertTrue(output.find(str(hours * perhour)) > -1, "Syötteellä {} oikeaa palkkaa {} ei löydy tulosteestasi {}".format(test_input, (hours * perhour), output))
            oikea = "Palkka {} euroa".format((hours * perhour))
            self.assertEqual(output, oikea, "Tulostus on väärässä muodossa, oikea tulostus on\n{}\nmutta ohjelmasi tulostaa\n{}".format(oikea,output))
    

if __name__ == '__main__':
    unittest.main()
