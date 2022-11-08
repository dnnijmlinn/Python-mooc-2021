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

@points('5.opiskelijarekisteri_osa3')
class OpiskelijarekisteriOsa3Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    def test_1_nollaa_ei_merkata(self):
        output_alussa = get_stdout()
        try:
            koodi = """opiskelijat = {}
lisaa_opiskelija(opiskelijat, "pekka")
lisaa_suoritus(opiskelijat, "pekka", ("ohpe", 0))
tulosta(opiskelijat, "pekka")"""
            lisaa_opiskelija = load(exercise, function1, 'fi')
            lisaa_suoritus = load(exercise, function3, 'fi')
            tulosta = load(exercise, function2, 'fi')
            opiskelijat = {}
            lisaa_opiskelija(opiskelijat, "pekka")
            lisaa_suoritus(opiskelijat, "pekka", ("ohpe", 0))
            tulosta(opiskelijat, "pekka")

            output_all = get_stdout().replace(output_alussa, '', 1)
            output = [l for l in output_all.split("\n") if len(l)>0 ]

            expr = """pekka:
 ei suorituksia"""
            exp = expr.split('\n')

        except:
            self.assertTrue(False, f"Varmista, että seuraavan ohjelmakoodin suoritus onnistuu\n\{koodi}" )

        self.assertFalse(len(output_all) == 0, f"Ohjelmasi pitäisi tulostaa {len(exp)} riviä kun suoritetaan seuraava koodi:\n{koodi}\nNyt se ei tulosta mitään" )
        self.assertEqual(len(output), len(exp), f"Ohjelmasi pitäisi tulostaa {len(exp)} riviä kun suoritetaan seuraava koodi:\n{koodi}\nNyt se tulostaa {len(output)} riviä:\n{output_all}" )
        for i in range(len(exp)):
            self.assertEqual(output[i].rstrip(), exp[i], f"Kun suoritetaan seuraava koodi:\n{koodi}\nTulostettavan rivin numero {i+1} pitäisi olla:\n{exp[i]}\nse on:\n{output[i]}" )

    def test_2_huonompaa_ei_huomioida(self):

        output_alussa = get_stdout()
        try:
            koodi = """opiskelijat = {}
lisaa_opiskelija(opiskelijat, "pekka")
lisaa_suoritus(opiskelijat, "pekka", ("ohpe", 5))
lisaa_suoritus(opiskelijat, "pekka", ("ohpe", 1))
tulosta(opiskelijat, "pekka")"""            
            lisaa_opiskelija = load(exercise, function1, 'fi')
            lisaa_suoritus = load(exercise, function3, 'fi')
            tulosta = load(exercise, function2, 'fi')
            opiskelijat = {}
            lisaa_opiskelija(opiskelijat, "pekka")
            lisaa_suoritus(opiskelijat, "pekka", ("ohpe", 5))
            lisaa_suoritus(opiskelijat, "pekka", ("ohpe", 1))

            tulosta(opiskelijat, "pekka")

            output_all = get_stdout().replace(output_alussa, '', 1)
            output = [l for l in output_all.split("\n") if len(l)>0 ]

            expr1 = """pekka:
 suorituksia 1 kurssilta:
  ohpe 5
 keskiarvo 5.0"""

            exp1 = expr1.split('\n')

        except:
            self.assertTrue(False, f"Varmista, että seuraavan ohjelmakoodin suoritus onnistuu\n{koodi}" )

        self.assertFalse(len(output_all) == 0, f"Ohjelmasi pitäisi tulostaa {len(exp1)} riviä kun suoritetaan seuraava koodi:\n{koodi}\nNyt se ei tulosta mitään" )
        self.assertEqual(len(output), len(exp1), f"Ohjelmasi pitäisi tulostaa {len(exp1)} riviä kun suoritetaan seuraava koodi:\n{koodi}\nNyt se tulostaa {len(output)} riviä:\n{output_all}" )
        for i in range(len(exp1)):
            self.assertTrue(output[i].rstrip() ==  exp1[i], f"Kun suoritetaan seuraava koodi:\n{koodi}\nTulostettavan rivin numero {i+1} pitäisi olla:\n{exp1[i]}\nse on:\n{output[i]}" )
    
    def test_3_arvosanan_voi_korottaa(self):

        output_alussa = get_stdout()
        try:

            koodi = """opiskelijat = {}
lisaa_opiskelija(opiskelijat, "pekka")
lisaa_suoritus(opiskelijat, "pekka", ("ohpe", 1))
lisaa_suoritus(opiskelijat, "pekka", ("ohpe", 5))
tulosta(opiskelijat, "pekka")"""

            lisaa_opiskelija = load(exercise, function1, 'fi')
            lisaa_suoritus = load(exercise, function3, 'fi')
            tulosta = load(exercise, function2, 'fi')
            opiskelijat = {}
            lisaa_opiskelija(opiskelijat, "pekka")
            lisaa_suoritus(opiskelijat, "pekka", ("ohpe", 1))
            lisaa_suoritus(opiskelijat, "pekka", ("ohpe", 5))

            tulosta(opiskelijat, "pekka")

            output_all = get_stdout().replace(output_alussa, '', 1)
            output = [l for l in output_all.split("\n") if len(l)>0 ]

            expr1 = """pekka:
 suorituksia 1 kurssilta:
  ohpe 5
 keskiarvo 5.0"""

            exp1 = expr1.split('\n')

        except:
            self.assertTrue(False, f"Varmista, että seuraavan ohjelmakoodin suoritus onnistuu\n{koodi}" )

        self.assertFalse(len(output_all) == 0, f"Ohjelmasi pitäisi tulostaa {len(exp1)} riviä kun suoritetaan seuraava koodi:\n{koodi}\nNyt se ei tulosta mitään" )
        self.assertEqual(len(output), len(exp1), f"Ohjelmasi pitäisi tulostaa {len(exp1)} riviä kun suoritetaan seuraava koodi:\n{koodi}\nNyt se tulostaa {len(output)} riviä:\n{output_all}" )
        for i in range(len(exp1)):
            self.assertTrue(output[i].rstrip() ==  exp1[i], f"Kun suoritetaan seuraava koodi:\n{koodi}\nTulostettavan rivin numero {i+1} pitäisi olla:\n{exp1[i]}\nse on:\n{output[i]}" )
    
    def test_4_suoritukset_tulostuvat(self):

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
tulosta(opiskelijat, "emilia")
tulosta(opiskelijat, "pekka")"""            
            lisaa_opiskelija = load(exercise, function1, 'fi')
            lisaa_suoritus = load(exercise, function3, 'fi')
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

            tulosta(opiskelijat, "emilia")
            tulosta(opiskelijat, "pekka")

            output_all = get_stdout().replace(output_alussa, '', 1)
            output = [l for l in output_all.split("\n") if len(l)>0 ]

            expr1 = """emilia:
 suorituksia 1 kurssilta:
  ohpe 5
 keskiarvo 5.0
pekka:
 suorituksia 2 kurssilta:
  tira 3
  jtkt 1
 keskiarvo 2.0"""

            expr2 = """emilia:
 suorituksia 1 kurssilta:
  ohpe 5
 keskiarvo 5.0
pekka:
 suorituksia 2 kurssilta:
  jtkt 1
  tira 3
 keskiarvo 2.0"""

            exp1 = expr1.split('\n')
            exp2 = expr2.split('\n')

        except:
            self.assertTrue(False, f"Varmista, että seuraavan ohjelmakoodin suoritus onnistuu\n\{koodi}" )

        self.assertFalse(len(output_all) == 0, f"Ohjelmasi pitäisi tulostaa {len(exp1)} riviä kun suoritetaan seuraava koodi:\n{koodi}\nNyt se ei tulosta mitään" )
        self.assertEqual(len(output), len(exp1), f"Ohjelmasi pitäisi tulostaa {len(exp1)} riviä kun suoritetaan seuraava koodi:\n{koodi}\nNyt se tulostaa {len(output)} riviä:\n{output_all}" )
        for i in range(len(exp1)):
            self.assertTrue(output[i].rstrip() ==  exp1[i] or output[i].rstrip() ==  exp2[i], f"Kun suoritetaan seuraava koodi:\n{koodi}\nTulostettavan rivin numero {i+1} pitäisi olla:\n{exp1[i]}\ntai\n{exp2[i]}\nse on:\n{output[i]}" )

if __name__ == '__main__':
    unittest.main()
