import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce

exercise = 'src.risuaitanelio'

def outputs_equal(str1 : str, str2 : str) -> bool:
    return str1.lower().replace(" ", "") == str2.lower().replace(" ", "")

def get_correct(s : str) -> str:
    w, h = s[1:-1].split(",")
    return "\n".join([(int(w) * "#") for i in range(int(h))])
   

@points('3.risuaitanelio')
class RisuaitanelioTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["1","1"]):
           cls.module = load_module(exercise, 'fi')


    def test_1_pienet_symmetriset(self):
        words = "(2,2) (5,5) (3,3) (6,6) (1,1)".split(" ")
        for word in words:
            with patch('builtins.input', side_effect = word[1:-1].split(",")):
                reload_module(self.module)
                output_all = get_stdout()
                output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
                correct = get_correct(word)
                w, h = [int(x) for x in word[1:-1].split(",")]
            
                self.assertFalse(len(output_all)==0, "Ohjelmasi ei tulosta mitään syötteellä "  + word)  
                self.assertTrue(len(output[0]) == w, f"Syötteellä {word} neliön leveyden pitäisi olla {w}, se oli {len(output[0])}. Ohjelmasi tulostus:\n{output_all}")
                self.assertTrue(len(output) == h, f"Syötteellä {word} neliön korkeuden pitäisi olla {h}, se oli {len(output)}. Ohjelmasi tulostus:\n{output_all}")
                self.assertTrue(outputs_equal(output_all, correct), "Ohjelmasi tuloste\n{}\nei vastaa oikeaa tulostetta \n{}\nsyötteellä {}".
                    format(output_all, correct, word))
    
    def test_2_suuret_symmetriset(self):
        words = "(10,10) (15,15) (8,8)".split(" ")
        for word in words:
            with patch('builtins.input', side_effect = word[1:-1].split(",")):
                reload_module(self.module)
                output_all = get_stdout()
                output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
                correct = get_correct(word)
                w, h = [int(x) for x in word[1:-1].split(",")]
            
                self.assertFalse(len(output_all)==0, "Ohjelmasi ei tulosta mitään syötteellä "  + word)  
                self.assertTrue(len(output[0]) == w, f"Syötteellä {word} neliön leveyden pitäisi olla {w}, se oli {len(output[0])}. Ohjelmasi tulostus:\n{output_all}")
                self.assertTrue(len(output) == h, f"Syötteellä {word} neliön korkeuden pitäisi olla {h}, se oli {len(output)}. Ohjelmasi tulostus:\n{output_all}")
                self.assertTrue(outputs_equal(output_all, correct), "Ohjelmasi tuloste\n{}\nei vastaa oikeaa tulostetta \n{} \nsyötteellä {}".
                    format(output_all, correct, word))

    def test_3_ei_symmetriset(self):
        words = "(5,3) (3,6) (8,4) (5,10)".split(" ")
        for word in words:
            with patch('builtins.input', side_effect = word[1:-1].split(",")):
                reload_module(self.module)
                output_all = get_stdout()
                output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
                correct = get_correct(word)
                w, h = [int(x) for x in word[1:-1].split(",")]
            
                self.assertFalse(len(output_all)==0, "Ohjelmasi ei tulosta mitään syötteellä "  + word)  
                self.assertTrue(len(output[0]) == w, f"Syötteellä {word} neliön leveyden pitäisi olla {w}, se oli {len(output[0])}. Ohjelmasi tulostus:\n{output_all}")
                self.assertTrue(len(output) == h, f"Syötteellä {word} neliön korkeuden pitäisi olla {h}, se oli {len(output)}. Ohjelmasi tulostus:\n{output_all}")
                self.assertTrue(outputs_equal(output_all, correct), "Ohjelmasi tuloste\n{}\nei vastaa oikeaa tulostetta \n{} \nsyötteellä {}".
                    format(output_all, correct, word))

if __name__ == '__main__':
    unittest.main()
