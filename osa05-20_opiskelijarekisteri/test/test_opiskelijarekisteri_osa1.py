import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.opiskelijarekisteri'
function1 = 'lisaa_opiskelija'
function2 = 'tulosta'

@points('5.opiskelijarekisteri_osa1')
class OpiskelijarekisteriOsa1Test(unittest.TestCase):
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

    def test_osa1_1_funktio_olemassa(self):
        try:
            from src.opiskelijarekisteri import lisaa_opiskelija
        except:
            self.assertTrue(False, f'Koodistasi pitäisi löytyä funktio {function1}(opiskelijat: dict, nimi: str)')
        try:
            lisaa_opiskelija = load(exercise, function1, 'fi')
            lisaa_opiskelija({}, "pekka")
        except:
            koodi = """opiskelijat = {}
lisaa_opiskelija(opiskelijat, "pekka")"""
            self.assertTrue(False, f'Varmista että funktiota voidaan kutsua seuraavasti:\n{koodi}')

    def test_osa1_2_funktio_olemassa(self):
        try:
            from src.opiskelijarekisteri import tulosta
        except:
            self.assertTrue(False, f'Koodistasi pitäisi löytyä funktio {function2}(opiskelijat: dict, nimi: str)')
        try:
            tulosta = load(exercise, function2, 'fi')
            koodi = """opiskelijat = {}
tulosta(opiskelijat, "pekka")"""
            tulosta({}, "pekka")
        except:
            self.assertTrue(False, f'Varmista että funktiota voidaan kutsua seuraavasti:{koodi}')


    def test_osa1_3_lisatty_tulostuu(self):

        output_alussa = get_stdout()
        try:

            koodi = """opiskelijat = {}
lisaa_opiskelija(opiskelijat, "pekka")
tulosta(opiskelijat, "pekka")"""

            lisaa_opiskelija = load(exercise, function1, 'fi')
            tulosta = load(exercise, function2, 'fi')
            opiskelijat = {}
            lisaa_opiskelija(opiskelijat, "pekka")
            tulosta(opiskelijat, "pekka")
            output_all = get_stdout().replace(output_alussa, '', 1)
            output = [l for l in output_all.split("\n") if len(l)>0 ]

            expr = """pekka:
 ei suorituksia"""
            exp = expr.split('\n')

        except:
            self.assertTrue(False, f"Varmista, että seuraavan ohjelmakoodin suoritus onnistuu\n{koodi}" )

        self.assertFalse(len(output_all) == 0, f"Ohjelmasi pitäisi tulostaa {len(exp)} riviä kun suoritetaan seuraava koodi:\n{koodi}\nNyt se ei tulosta mitään" )
        self.assertEqual(len(output), len(exp), f"Ohjelmasi pitäisi tulostaa {len(exp)} riviä kun suoritetaan seuraava koodi:\n{koodi}\nNyt se tulostaa {len(output)} riviä:\n{output_all}" )
        for i in range(len(exp)):
            self.assertEqual(output[i].rstrip(), exp[i], f"Kun suoritetaan seuraava koodi:\n{koodi}\nTulostettavan rivin numero {i+1} pitäisi olla:\n{exp[i]}\nse on:\n{output[i]}" )

    def test_osa1_4_lisaamaton_tulostaa_huomautuksen(self):

        output_alussa = get_stdout()
        try:
            lisaa_opiskelija = load(exercise, function1, 'fi')
            tulosta = load(exercise, function2, 'fi')
            opiskelijat = {}
            lisaa_opiskelija(opiskelijat, "pekka")
            tulosta(opiskelijat, "emilia")
            output_all = get_stdout().replace(output_alussa, '', 1)
            output = [l for l in output_all.split("\n") if len(l)>0 ]

            koodi = """opiskelijat = {}
lisaa_opiskelija(opiskelijat, "pekka")
tulosta(opiskelijat, "emilia")"""

            expr = """ei löytynyt ketään nimellä emilia"""
            exp = expr.split('\n')

        except:
            self.assertTrue(False, f"Varmista, että seuraavan ohjelmakoodin suoritus onnistuu\n\{koodi}" )

        self.assertFalse(len(output_all) == 0, f"Ohjelmasi pitäisi tulostaa {len(exp)} riviä kun suoritetaan seuraava koodi:\n{koodi}\nNyt se ei tulosta mitään" )
        self.assertEqual(len(output), len(exp), f"Ohjelmasi pitäisi tulostaa {len(exp)} riviä kun suoritetaan seuraava koodi:\n{koodi}\nNyt se tulostaa {len(output)} riviä:\n{output_all}" )
        for i in range(len(exp)):
            self.assertEqual(output[i].rstrip(), exp[i], f"Kun suoritetaan seuraava koodi:\n{koodi}\nTulostettavan rivin numero {i+1} pitäisi olla:\n{exp[i]}\nse on:\n{output[i]}" )

    def test_osa1_5_monta_listausta_toimii(self):

        koodi = """opiskelijat = {}
lisaa_opiskelija(opiskelijat, "pekka")
lisaa_opiskelija(opiskelijat, "emilia")
tulosta(opiskelijat, "pekka")
tulosta(opiskelijat, "emilia")
tulosta(opiskelijat, "antti")
"""

        output_alussa = get_stdout()
        try:
            lisaa_opiskelija = load(exercise, function1, 'fi')
            tulosta = load(exercise, function2, 'fi')
            opiskelijat = {}
            lisaa_opiskelija(opiskelijat, "pekka")
            lisaa_opiskelija(opiskelijat, "emilia")
            tulosta(opiskelijat, "pekka")
            tulosta(opiskelijat, "emilia")
            tulosta(opiskelijat, "antti")
            output_all = get_stdout().replace(output_alussa, '', 1)
            output = [l for l in output_all.split("\n") if len(l)>0 ]

            expr = """pekka:
 ei suorituksia
emilia:
 ei suorituksia
ei löytynyt ketään nimellä antti"""
            exp = expr.split('\n')

        except:
            self.assertTrue(False, f"Varmista, että seuraavan ohjelmakoodin suoritus onnistuu\n\{koodi}" )

        self.assertFalse(len(output_all) == 0, f"Ohjelmasi pitäisi tulostaa {len(exp)} riviä kun suoritetaan seuraava koodi:\n{koodi}\nNyt se ei tulosta mitään" )
        self.assertEqual(len(output), len(exp), f"Ohjelmasi pitäisi tulostaa {len(exp)} riviä kun suoritetaan seuraava koodi:\n{koodi}\nNyt se tulostaa {len(output)} riviä:\n{output_all}" )
        for i in range(len(exp)):
            self.assertEqual(output[i].rstrip(), exp[i], f"Kun suoritetaan seuraava koodi:\n{koodi}\nTulostettavan rivin numero {i+1} pitäisi olla:\n{exp[i]}\nse on:\n{output[i]}" )


if __name__ == '__main__':
    unittest.main()
