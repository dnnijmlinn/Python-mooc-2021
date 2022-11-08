import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.omistuskirjoitus'

def format(a):
    return "\n".join(a)

def get_content(tiedosto):
    with open(tiedosto) as f:
        return [x.replace("\n","") for x in f.readlines() if len(x.strip()) > 0]

@points('6.omistuskirjoitus')
class OmistuskirjotusTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["Arto", "omistettu.txt"]*10):
           cls.module = load_module(exercise, 'fi')
    
    def test_omistuskirjoitus_onnistuu(self):
        for nimi, tiedosto in [
                ("Arto", "omistettu.txt"),
                ("Lea", "omistus.txt"),
                ("John Doe", "book_cover_page.txt"),
                ("Sebastian", "kasivarsi.txt"),
                ("Jori", "foobar.txt"),
            ]:
            with patch('builtins.input', side_effect=[nimi, tiedosto, AssertionError("Ohjelmasi lukee syötettä liian monta kertaa")]):
                reload_module(self.module)
                output = get_stdout()
                
                try:
                    content = get_content(tiedosto)
                except:
                    mssage = """\nHuomaa, että tässä tehtävässä mitään koodia EI TULE SIJOITTAA lohkon
if __name__ == "__main__":
sisälle
"""
            #\n{mssage}") 
                    self.assertTrue(False, f"Ohjelmasi tulisi kirjoittaa syötteellä\n{nimi}\n{tiedosto}\nomistuskirjoitus tiedostoon {tiedosto}\n{mssage}")


                correct = f"Hei {nimi}, toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi"
                self.assertTrue(len(content) == 1, f"Tiedostossa {tiedosto} pitäisi olla nyt yksi rivi, tiedoston sisältö on kuitenkin:\n{format(content)}")
                self.assertTrue(content[0].strip() == correct, f"Tiedoston {tiedosto} sisällön pitäisi olla \n{correct}\nmutta se on \n{format(content)}")

if __name__ == '__main__':
    unittest.main()
