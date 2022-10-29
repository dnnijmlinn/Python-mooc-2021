import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.tarina'

def p(a):
    return "\n".join(a)

testset = [
    ['hei', 'maailma', 'loppu'],
    'Olipa kerran pieni talo preerialla'.split(' ') + ['loppu'],
    'Alussa oli suo kuokka ja Jussi'.split(' ') + ['loppu'],
    'Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'.split(' ') + ['loppu'],
    'Ohjelmoinnin perusteet on viiden opintopisteen laajuinen tietojenkäsittelytieteen perusopintokurssi Kesällä 2020 kurssi järjestetään ensimmäistä kertaa Python-kielellä Kurssi muodostuu viikoittaisista tehtävistä sekä kokeesta kurssin lopussa'.split(' ') + ['loppu']
]

testset2 = [
    ['hei', 'maailma', 'maailma'],
    'Olipa kerran pieni talo preerialla'.split(' ') + ['preerialla'],
    'Alussa oli suo kuokka ja Jussi'.split(' ') + ['Jussi'],
    'Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'.split(' ') + ['aliqua'],
    'Ohjelmoinnin perusteet on viiden opintopisteen laajuinen tietojenkäsittelytieteen perusopintokurssi Kesällä 2020 kurssi järjestetään ensimmäistä kertaa Python-kielellä Kurssi muodostuu viikoittaisista tehtävistä sekä kokeesta kurssin lopussa'.split(' ') + ['lopussa']
]

class TarinaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["loppu"] * 10):
           cls.module = load_module(exercise, 'fi')

    @points('2.tarina-osa1')
    def test_osa1a(self):
        values = "hei hei loppu".split(" ")
        with patch('builtins.input', side_effect = values):
            try:
                reload_module(self.module)
                output = get_stdout()  
            except:
                self.assertTrue(False, "Varmista, että ohjelma lopettaa toiminnan syötteellä\n{}".format(p(values)))

    @points('2.tarina-osa1')
    def test_osa1b(self):
       for *alku, loppu  in testset: 
        with patch('builtins.input', side_effect= alku + [loppu, AssertionError("Syötettä pyydetään liian monta kertaa.") ], ) as prompt:
            reload_module(self.module)
            output = get_stdout()  

            inpt = '\n'.join(alku) + "\n" + loppu 

            expected = ' '.join(alku)
            self.assertTrue(len(output)>0, f"Ohjelmasi ei tulostanut mitään syötteellä\n{inpt}" )
            self.assertEqual(expected.strip(), output.strip(), f"Syötteellä\n{inpt}\nohjelmasi pitäisi tulostaa:\n{expected}\nohjelmasi tulosti:\n{output}" )

    @points('2.tarina-osa2')
    def test_osa2a(self):
        values = "hei hei".split(" ")
        with patch('builtins.input', side_effect = values):
            try:
                reload_module(self.module)
                output = get_stdout()  
            except:
                self.assertTrue(False, "Varmista, että ohjelma lopettaa toiminnan syötteellä\n{}".format(p(values)))

    @points('2.tarina-osa2')
    def test_osa2b(self):
       for *alku, loppu in testset2: 
        with patch('builtins.input', side_effect= alku + [loppu, AssertionError("Syötettä pyydetään liian monta kertaa.") ], ) as prompt:
            reload_module(self.module)
            output = get_stdout()  

            inpt = '\n'.join(alku) + " " + loppu 

            expected = ' '.join(alku)
            self.assertEqual(expected.strip(), output.strip(), f"Syötteellä\n{inpt}\nohjelmasi pitäisi tulostaa:\n{expected}\nohjelmasi tulosti:\n{output}" )

if __name__ == '__main__':
    unittest.main()
