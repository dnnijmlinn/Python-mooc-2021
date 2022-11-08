import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.vanhin_henkiloista'
function = 'vanhin'


@points('5.vanhin_henkiloista')
class VanhinTest(unittest.TestCase):
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
            from src.vanhin_henkiloista import vanhin
        except:
            self.assertTrue(False, f'Koodistasi pitäisi löytyä funktio nimeltä vanhin(henkilot: list)')
        try:
            vanhin = load(exercise, function, 'fi')
            koodi = """hlista = [("Arto", 1977), ("Milla", 2014)]
vanhin(hlista)"""

            hlista = [("Arto", 1977), ("Milla", 2014)]
            vanhin(hlista)

        except:
            self.assertTrue(False, f'Tarkista että funktiota voi kutsua seuraavasti:\n{koodi}')


    def test_2_paluuarvon_tyyppi(self):
        vanhin = load(exercise, function, 'fi')
        koodi = """hlista = [("Arto", 1977), ("Milla", 2014)]
vastaus = vanhin(hlista)"""

        hlista = [("Arto", 1977), ("Milla", 2014)]
        vastaus = vanhin(hlista)

        self.assertTrue(type(vastaus) == str, f"Funktio {function} ei palauta merkkijonoa arvoa kun suoritetaan koodi:\n{koodi}")

    def test_3_toiminnallisuus(self):
        vanhin = load(exercise, function, 'fi')
        for hlista in [ 
                [("Arto", 1977), ("Milla", 2014)],
                [("Milla", 2014), ("Arto", 1977)],
                [("Milla", 2014), ("Arto", 1977), ("Einari", 1985),  ("Maija", 1953), ("Essi", 1997)],
                [("Leevi", 2016), ("Elias", 2019), ("Eero", 2012),  ("Venla", 2013), ("Jane Doe", 2020)],
                [("Donald", 1982), ("Daisy", 1892), ("Angela", 1965),  ("Vladimir", 2000), ("Dunja", 1919), ("Tellervo", 1921)]
            ]:
            koodi = f"hlista = {hlista}\n"+"vastaus = vanhin(hlista)"
            vastaus = vanhin(hlista)
            oikea = [ n for n, i in hlista if i == min( i for n, i in hlista)][0]

            self.assertEqual(vastaus, oikea, f"Funktino {function} palauttama {vastaus} on väärin, sen pitäisi palauttaa {oikea} kun suoritetaan koodi\n{koodi}")

if __name__ == '__main__':
    unittest.main()
