import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.opiskelijarekisteri'
function1 = 'lisaa_opiskelija'
function2 = 'tulosta'
function3 = 'lisaa_suoritus'
function4 = 'kooste'

@points('5.opiskelijarekisteri_osa4')
class OpiskelijarekisteriOsa4Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    def test_osa4_1_funktio_olemassa(self):
        try:
            from src.opiskelijarekisteri import kooste
        except:
            self.assertTrue(False, f'Koodistasi pitäisi löytyä funktio {function4}(opiskelijat: dict)')
       
        try:
            lisaa_opiskelija = load(exercise, function1, 'fi')
            lisaa_suoritus = load(exercise, function3, 'fi')
            kooste = load(exercise, function4, 'fi')

            opiskelijat = {}
            lisaa_opiskelija(opiskelijat, "pekka")
            lisaa_suoritus(opiskelijat, "pekka", ("ohpe", 5))
            kooste(opiskelijat)
        except:
            koodi = """opiskelijat = {}
lisaa_opiskelija(opiskelijat, "pekka")
lisaa_suoritus(opiskelijat, "pekka", ("ohpe", 5))
kooste(opiskelijat)"""
            self.assertTrue(False, f',Varmista että funktiota voidaan kutsua seuraavasti:\n{koodi}')

    def test_osa4_2_tulostus_oikein(self):
        output_alussa = get_stdout()
        try:
            koodi = """opiskelijat = {}
lisaa_opiskelija(opiskelijat, "pekka")
lisaa_suoritus(opiskelijat, "pekka", ("ohpe", 5))
kooste(opiskelijat)"""            
            lisaa_opiskelija = load(exercise, function1, 'fi')
            lisaa_suoritus = load(exercise, function3, 'fi')
            kooste = load(exercise, function4, 'fi')
            tulosta = load(exercise, function2, 'fi')

            opiskelijat = {}
            lisaa_opiskelija(opiskelijat, "pekka")
            lisaa_suoritus(opiskelijat, "pekka", ("ohpe", 5))
            kooste(opiskelijat)

            output_all = get_stdout().replace(output_alussa, '', 1)
            output = [l for l in output_all.split("\n") if len(l)>0 ]

            expr = """opiskelijoita 1
eniten suorituksia 1 pekka
paras keskiarvo 5.0 pekka"""
            exp = expr.split('\n')

        except:
            self.assertTrue(False, f"Varmista, että seuraavan ohjelmakoodin suoritus onnistuu\n\{koodi}" )

        self.assertFalse(len(output_all) == 0, f"Ohjelmasi pitäisi tulostaa {len(exp)} riviä kun suoritetaan seuraava koodi:\n{koodi}\nNyt se ei tulosta mitään" )
        self.assertEqual(len(output), len(exp), f"Ohjelmasi pitäisi tulostaa {len(exp)} riviä kun suoritetaan seuraava koodi:\n{koodi}\nNyt se tulostaa {len(output)} riviä:\n{output_all}" )
        for i in range(len(exp)):
            self.assertEqual(output[i].rstrip(), exp[i], f"Kun suoritetaan seuraava koodi:\n{koodi}\nTulostettavan rivin numero {i+1} pitäisi olla:\n{exp[i]}\nse on:\n{output[i]}" )


    def test_osa4_3_tulostus_oikein(self):
        output_alussa = get_stdout()
        try:

            koodi = """opiskelijat = {}
lisaa_opiskelija(opiskelijat, "emilia")
lisaa_opiskelija(opiskelijat, "pekka")
lisaa_suoritus(opiskelijat, "emilia", ("ohpe", 4))
lisaa_suoritus(opiskelijat, "emilia", ("ohpe", 5))
lisaa_suoritus(opiskelijat, "pekka", ("tira", 3))
lisaa_suoritus(opiskelijat, "pekka", ("lama", 0))
lisaa_suoritus(opiskelijat, "pekka", ("tira", 2))
lisaa_suoritus(opiskelijat, "pekka", ("jtkt", 1))
lisaa_suoritus(opiskelijat, "pekka", ("ohtu", 3))
kooste(opiskelijat)
kooste(opiskelijat)"""


            lisaa_opiskelija = load(exercise, function1, 'fi')
            lisaa_suoritus = load(exercise, function3, 'fi')
            kooste = load(exercise, function4, 'fi')
            tulosta = load(exercise, function2, 'fi')

            opiskelijat = {}
            lisaa_opiskelija(opiskelijat, "emilia")
            lisaa_opiskelija(opiskelijat, "pekka")
            lisaa_suoritus(opiskelijat, "emilia", ("ohpe", 4))
            lisaa_suoritus(opiskelijat, "emilia", ("ohpe", 5))
            lisaa_suoritus(opiskelijat, "pekka", ("tira", 3))
            lisaa_suoritus(opiskelijat, "pekka", ("lama", 0))
            lisaa_suoritus(opiskelijat, "pekka", ("tira", 2))
            lisaa_suoritus(opiskelijat, "pekka", ("jtkt", 1))
            lisaa_suoritus(opiskelijat, "pekka", ("ohtu", 3))
            kooste(opiskelijat)

            output_all = get_stdout().replace(output_alussa, '', 1)
            output = [l for l in output_all.split("\n") if len(l)>0 ]

            expr = """opiskelijoita 2
eniten suorituksia 3 pekka
paras keskiarvo 5.0 emilia"""
            exp = expr.split('\n')

        except:
            self.assertTrue(False, f"Varmista, että seuraavan ohjelmakoodin suoritus onnistuu\n\{koodi}" )

        self.assertFalse(len(output_all) == 0, f"Ohjelmasi pitäisi tulostaa {len(exp)} riviä kun suoritetaan seuraava koodi:\n{koodi}\nNyt se ei tulosta mitään" )
        self.assertEqual(len(output), len(exp), f"Ohjelmasi pitäisi tulostaa {len(exp)} riviä kun suoritetaan seuraava koodi:\n{koodi}\nNyt se tulostaa {len(output)} riviä:\n{output_all}" )
        for i in range(len(exp)):
            self.assertEqual(output[i].rstrip(), exp[i], f"Kun suoritetaan seuraava koodi:\n{koodi}\nTulostettavan rivin numero {i+1} pitäisi olla:\n{exp[i]}\nse on:\n{output[i]}" )


if __name__ == '__main__':
    unittest.main()
