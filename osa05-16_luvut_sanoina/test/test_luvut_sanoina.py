import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.luvut_sanoina'
function = 'lukukirja'

def get_correct() -> dict:
    return {0: 'nolla', 1: 'yksi', 2: 'kaksi', 3: 'kolme', 4: 'neljä', 5: 'viisi', 6: 'kuusi', 7: 'seitsemän', 8: 'kahdeksan', 9: 'yhdeksän', 10: 'kymmenen', 
    11: 'yksitoista', 12: 'kaksitoista', 13: 'kolmetoista', 14: 'neljätoista', 15: 'viisitoista', 16: 'kuusitoista', 17: 'seitsemäntoista', 18: 'kahdeksantoista', 
    19: 'yhdeksäntoista', 20: 'kaksikymmentä', 21: 'kaksikymmentäyksi', 22: 'kaksikymmentäkaksi', 23: 'kaksikymmentäkolme', 24: 'kaksikymmentäneljä', 
    25: 'kaksikymmentäviisi', 26: 'kaksikymmentäkuusi', 27: 'kaksikymmentäseitsemän', 28: 'kaksikymmentäkahdeksan', 29: 'kaksikymmentäyhdeksän', 30: 'kolmekymmentä', 
    31: 'kolmekymmentäyksi', 32: 'kolmekymmentäkaksi', 33: 'kolmekymmentäkolme', 34: 'kolmekymmentäneljä', 35: 'kolmekymmentäviisi', 36: 'kolmekymmentäkuusi', 
    37: 'kolmekymmentäseitsemän', 38: 'kolmekymmentäkahdeksan', 39: 'kolmekymmentäyhdeksän', 40: 'neljäkymmentä', 41: 'neljäkymmentäyksi', 42: 'neljäkymmentäkaksi', 
    43: 'neljäkymmentäkolme', 44: 'neljäkymmentäneljä', 45: 'neljäkymmentäviisi', 46: 'neljäkymmentäkuusi', 47: 'neljäkymmentäseitsemän', 48: 'neljäkymmentäkahdeksan', 
    49: 'neljäkymmentäyhdeksän', 50: 'viisikymmentä', 51: 'viisikymmentäyksi', 52: 'viisikymmentäkaksi', 53: 'viisikymmentäkolme', 54: 'viisikymmentäneljä',
     55: 'viisikymmentäviisi', 56: 'viisikymmentäkuusi', 57: 'viisikymmentäseitsemän', 58: 'viisikymmentäkahdeksan', 59: 'viisikymmentäyhdeksän', 60: 'kuusikymmentä', 
     61: 'kuusikymmentäyksi', 62: 'kuusikymmentäkaksi', 63: 'kuusikymmentäkolme', 64: 'kuusikymmentäneljä', 65: 'kuusikymmentäviisi', 66: 'kuusikymmentäkuusi', 
     67: 'kuusikymmentäseitsemän', 68: 'kuusikymmentäkahdeksan', 69: 'kuusikymmentäyhdeksän', 70: 'seitsemänkymmentä', 71: 'seitsemänkymmentäyksi', 72: 'seitsemänkymmentäkaksi', 
     73: 'seitsemänkymmentäkolme', 74: 'seitsemänkymmentäneljä', 75: 'seitsemänkymmentäviisi', 76: 'seitsemänkymmentäkuusi', 77: 'seitsemänkymmentäseitsemän', 
     78: 'seitsemänkymmentäkahdeksan', 79: 'seitsemänkymmentäyhdeksän', 80: 'kahdeksankymmentä', 81: 'kahdeksankymmentäyksi', 82: 'kahdeksankymmentäkaksi', 
     83: 'kahdeksankymmentäkolme', 84: 'kahdeksankymmentäneljä', 85: 'kahdeksankymmentäviisi', 86: 'kahdeksankymmentäkuusi', 87: 'kahdeksankymmentäseitsemän', 
     88: 'kahdeksankymmentäkahdeksan', 89: 'kahdeksankymmentäyhdeksän', 90: 'yhdeksänkymmentä', 91: 'yhdeksänkymmentäyksi', 92: 'yhdeksänkymmentäkaksi', 93: 'yhdeksänkymmentäkolme', 
     94: 'yhdeksänkymmentäneljä', 
    95: 'yhdeksänkymmentäviisi', 96: 'yhdeksänkymmentäkuusi', 97: 'yhdeksänkymmentäseitsemän', 98: 'yhdeksänkymmentäkahdeksan', 99: 'yhdeksänkymmentäyhdeksän'}

def output(d: dict):
    for key in sorted(d.keys()):
        print(str(key) + ": " + str(d[key]))

@points('5.luvut_sanoina')
class LuvutSanoinaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    def test_0_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    def test_1_funktio_olemassa(self):
        try:
            from src.luvut_sanoina import lukukirja
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä lukukirja')
        try:
            lukukirja()
        except:
            self.assertTrue(False, 'Varmista että seuraava funktiokutsu toimii lukukirja()')

    def test_2_paluuarvon_tyyppi(self):
        lukukirja = load(exercise, function, 'fi')
        val = lukukirja()
        taip = str(type(val)).replace("<class '", '').replace("'>","")
        self.assertTrue(type(val) == dict, f"Funktion {function} tulisi palauttaa sanakirja, nyt se palauttaa arvon tyyppiä {taip}.")

    def test_3_testaa_lukuja(self):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
            reload_module(self.module)
            output_alussa = get_stdout()
            lukukirja = load(exercise, function, 'fi')

            luvut = lukukirja()

            self.assertEqual(100, len(luvut), f"Palautetussa sanakirjassa pitäisi olla 100 alkiota, mutta siinä on {len(luvut)} alkiota: \n{luvut}")

            tests = get_correct()
            for i in range(100):
                self.assertEqual(tests[i], luvut[i], f"Sanakirjan arvo {luvut[i]} ei vastaa mallivastausta {tests[i]} avaimen arvolla {i}")

if __name__ == '__main__':
    unittest.main()
