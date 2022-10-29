import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce

exercise = 'src.sanalaatikko'

def outputs_equal(str1 : str, str2 : str) -> bool:
    return sanitize(str1.lower()) == sanitize(str2.lower())

def get_correct(s : str) -> str:
    s1 = "*" * 30
    s2 = "*" + (28 - len(s)) // 2 * " " + s + (28 -len(s)) // 2 * " "
    if len(s) % 2 == 1:
        s2 += " "
    return s1 + "\n" + s2 + "*\n" + s1
   
def get_correct2(s : str) -> str:
    s1 = "*" * 30
    s2 = (28 - len(s)) // 2 * " " + s + (28 -len(s)) // 2 * " "
    if len(s) % 2 == 1:
        s2 = " " + s2
    return s1 + "\n*" + s2 + "*\n" + s1

@points('3.sanalaatikko')
class SanalaatikkoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value="a"):
           cls.module = load_module(exercise, 'fi')

    def test_lyhyet_sanat(self):
        words = "testi heippa simsalabim zorro viuh!".split(" ")
        for word in words:
            with patch('builtins.input', return_value = word):
                reload_module(self.module)
                output_all = get_stdout()
                output = [x.strip() for x in output_all.split("\n") if len(x.strip()) > 0]
                correct = get_correct(word)
            
                self.assertFalse(len(output_all)==0, "Ohjelmasi ei tulosta mitään syötteellä "  + word)  
                self.assertTrue(len(output) == 3, "Ohjelmasi tulostaa syötteellä {} {} rivin sijasta {} riviä".
                    format(word, 3, len(output)))

                self.assertEqual(output[0], "*" * 30, "Tulosteesi eka rivi ei koostu 30 tähdestä: {}".format(output[0]))
                self.assertEqual(output[2], "*" * 30, "Tulosteesi viimeinen rivi ei koostu 30 tähdestä: {}".
                    format(output[2]))

                self.assertTrue(len(output[1]) == 30, "Keskimmäisen rivin pituus ei ole 30 vaan {} kun syöte on {}: \n{}". 
                    format(len(output[1]), word, output[1]))

                correct2 = get_correct2(word)
                self.assertTrue(outputs_equal(output_all, correct) or outputs_equal(output_all, correct2), "Ohjelmasi tuloste\n{}\nei vastaa oikeaa tulostetta \n{}\nsyötteellä {}".
                    format(output_all, correct, word))

    def test_pitkat_sanat(self):
        words = ["Tämä on pidempi lause.", "simsalabim, sanoi taikuri", "123456789012345678901234567", "abcdefgacbdefg"]
        for word in words:
            with patch('builtins.input', return_value = word):
                reload_module(self.module)
                output_all = get_stdout()
                output = [x.strip() for x in output_all.split("\n") if len(x.strip()) > 0]
                correct = get_correct(word)
            
                self.assertFalse(len(output_all)==0, "Ohjelmasi ei tulosta mitään syötteellä "  + word)  
                self.assertTrue(len(output) == 3, "Ohjelmasi tulostaa syötteellä {} {} rivin sijasta {} riviä".
                    format(word, 3, len(output)))

                self.assertEqual(output[0], "*" * 30, "Tulosteesi eka rivi ei koostu 30 tähdestä: {}".format(output[0]))
                self.assertEqual(output[2], "*" * 30, "Tulosteesi viimeinen rivi ei koostu 30 tähdestä: {}".
                    format(output[2]))

                self.assertTrue(len(output[1]) == 30, "Keskimmäisen rivin pituus ei ole 30 vaan {} kun syöte on {}: \n{}". 
                    format(len(output[1]), word, output[1]))
                
                correct2 = get_correct2(word)
                self.assertTrue(outputs_equal(output_all, correct) or outputs_equal(output_all, correct2), "Ohjelmasi tuloste\n{}\nei vastaa oikeaa tulostetta \n{}\nsyötteellä {}".
                    format(output_all, correct, word))

if __name__ == '__main__':
    unittest.main()
