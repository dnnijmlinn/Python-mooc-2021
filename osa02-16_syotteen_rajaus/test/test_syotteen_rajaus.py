import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce
from random import randint

exercise = 'src.syotteen_rajaus'

def p(a):
    return "\n".join(a)

@points('2.syotteen_rajaus')
class SyotteenRajausTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["0"]):
            cls.module = load_module(exercise, 'fi')

    def test_1_lopetus(self):
        values = "1 0".split(" ")
    
        with patch('builtins.input', side_effect = values):
            try:
                reload_module(self.module)
                output = get_stdout()
            except:
                self.assertTrue(False, f"Varmista, että ohjelma lopettaa toiminnan syötteellä:\n{p(values)}")

    def test_2_lukuja_ja_lopetus(self):
        values = "9 4 16 1 0".split(" ")
        correct = "3.0\n2.0\n4.0\n1.0\nLopetetaan..."

        with patch('builtins.input', side_effect = values):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output)>0, f"Ohjelmasi ei tulosta mitään syötteellä\n:{p(values)}")
            
            self.assertTrue(len(output.split("\n")) == 5, "Ohjelmasi tulostaa kyselyjen lisäksi viiden sijasta {} riviä\n{}\nkun syöte on\n{}".format(len(output.split("\n")), output, p(values)))
            self.assertTrue(sanitize(output) == sanitize(correct), "Tulostus \n{} \nei vastaa oikeaa tulostetta \n{} \nkun syöte on\n{}".
                format(output, correct, p(values)))

    def test_3_epakelpo(self):
        values = "-1 0".split(" ")

        with patch('builtins.input', side_effect = values):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, f"Varmista, että ohjelmasi toimii syötteellä\n:{p(values)}")

    def test_4_lukuja_epakelpo_ja_lopetus(self):
        values = "9 4 16 -1 0".split(" ")
        correct = "3.0\n2.0\n4.0\nEpäkelpo luku\nLopetetaan..."

        with patch('builtins.input', side_effect = values):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, "Varmista, että ohjelmasi toimii syötteellä\n:{}".format(p(values)))

            output = get_stdout()
            self.assertTrue(len(output)>0, f"Ohjelmasi ei tulosta mitään syötteellä\n:{p(values)}")
            self.assertTrue(len(output.split("\n")) == 5, "Ohjelmasi tulostaa kyselyjen lisäksi viiden sijasta {} riviä:\n{}\nkun syöte on\n{}".format(len(output.split("\n")), output, p(values)))
            self.assertTrue(sanitize(output) == sanitize(correct), "Tulostus \n{} \nei vastaa oikeaa tulostetta \n{} \nkun syöte on\n{}".
                format(output, correct, p(values)))

    def test_5_pelkka_lopetus(self):
        values = "0".split(" ")
        correct = "Lopetetaan..."

        with patch('builtins.input', side_effect = values):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output)>0, f"Ohjelmasi ei tulosta mitään syötteellä {p(values)}")
            self.assertTrue(len(output.split("\n")) == 1, "Ohjelmasi tulostaa kyselyjen lisäksi yhden sijasta {} riviä:\n{}\nkun syöte on\n{}".format(len(output.split("\n")), output, p(values)))
            self.assertTrue(sanitize(output) == sanitize(correct), "Tulostus \n{} \nei vastaa oikeaa tulostetta \n{} \nkun syöte on\n{}".
                format(output, correct, p(values)))

if __name__ == '__main__':
    unittest.main()
