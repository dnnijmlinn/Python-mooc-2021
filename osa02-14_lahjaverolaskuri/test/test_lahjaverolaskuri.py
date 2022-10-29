import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.lahjaverolaskuri'

@points('2.lahjaverolaskuri')
class LahjaverolaskuriTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_arvot(self):
        values = ["11400 612", "42450 3445", "195000 21500", "567800 77270", "10100200 1689134"]
        for valuegroup in values:
            testvalue, correct = valuegroup.split(" ")
            with patch('builtins.input', return_value = testvalue):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Ohjelmasi ei tulosta mitään syötteellä {}".format(valuegroup.split(' ')[0]))

                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä: {} kun syöte on {}".format(len(output), output, testvalue))
                oikea = "Vero: "+str(float(correct)) + " euroa"
                self.assertTrue(output[0].strip().find("Vero: ")  > -1, "Tulostus oli\n{}\nsen pitäisi olla \n{}\nkun syöte on {}".
                    format(output[0], oikea, testvalue))
                kohta = output[0].strip().find("Vero: ")+len("Vero: ")
                luku = [x for x in output[0].strip()[kohta:].split(' ') if len(x)>0][0]
                self.assertTrue(luku.find(correct) > -1, "Tulostus\n{}\nei sisällä oikeaa tulosta\n{}\nkun syöte on {}".
                    format(output[0], correct, testvalue))

    def test_ei_veroa(self):
        values = [str(randint(0, 4999)) for i in range(5)]
        for testvalue in values:
            correct = "Ei veroa"
            with patch('builtins.input', return_value = testvalue):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Ohjelmasi ei tulosta mitään syötteellä {}".format(testvalue.split(' ')[0]))

                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä: {} kun syöte on {}".format(len(output), output, testvalue))
                self.assertTrue(output[0].lower().strip().find(correct.lower()) > -1, "Tulostus\n{}\nei sisällä oikeaa tulosta\n{}\nkun syöte on {}".
                    format(output[0], correct, testvalue))
    
if __name__ == '__main__':
    unittest.main()
