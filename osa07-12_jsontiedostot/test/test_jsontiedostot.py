import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.jsontiedostot'

import os
from shutil import copyfile

testdata = ['tiedosto1.json', 'tiedosto2.json', 'tiedosto3.json', 'tiedosto4.json']

def f(p):
    return "\n".join(p)

@points('7.jsontiedostot')
class JsonTiedostotTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
            for filename in testdata:
                data_file = os.path.join('test', filename)
                copyfile(data_file, filename)      
            cls.module = load_module(exercise, 'fi')

    @classmethod
    def tearDownClass(cls):
        for filename in testdata:
            os.remove(filename)

    def test_0a_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    def test1_funktio_olemssa(self):
        try:
             from src.jsontiedostot import tulosta_henkilot
        except:
            self.assertTrue(False, f'Koodistasi pitäisi löytyä funktio nimeltä tulosta_henkilot(tiedosto: str)')
        
        try:  
            tulosta_henkilot("tiedosto1.json")
        except:
            self.assertTrue(False, f'Varmista että seuraava funktiokutsu onnistuu tulosta_henkilot("tiedosto1.json")')

    def test_2_toimii_tiedostolla1(self):
        from src.jsontiedostot import tulosta_henkilot
        output_alussa = get_stdout()
        tulosta_henkilot("tiedosto1.json")
        koodi = 'tulosta_henkilot("tiedosto1.json")'
        output_all = get_stdout().replace(output_alussa, '', 1)
        output = [l for l in output_all.split("\n") if len(l)>0 ]
        
        correct = """Pekka Pythonisti 27 vuotta (koodaus, kutominen)
Jaana Javanainen 24 vuotta (koodaus, kalliokiipeily, lukeminen)"""

        cLines = correct.split('\n')
        self.assertTrue(len(output_all)>0, f'Kun suoritetaan {koodi}, ei tulostettu mitään')
        self.assertEqual(len(cLines),len(output), f'Kun suoritetaan {koodi}, pitäisi tulostaa {len(cLines)} riviä. Tulostettiin {len(output)} riviä:\n{f(output)}')
        for rivi in cLines:
            self.assertTrue(rivi in output, f'Kun suoritetaan {koodi}, pitäisi tulostuksesta löytyä rivi\n{rivi}\nTulostettiin\n{f(output)}')         
        for rivi in output:
            self.assertTrue(rivi in correct, f'Kun suoritetaan {koodi}, sisälsi tulostus seuraavan rivin\n{rivi}\nOikea tulostus sisältää vaan seuraavat rivit\n{f(correct)}')         

    def test_2_toimii_tiedostolla2(self):
        from src.jsontiedostot import tulosta_henkilot
        output_alussa = get_stdout()
        tulosta_henkilot("tiedosto2.json")
        koodi = 'tulosta_henkilot("tiedosto2.json")'
        output_all = get_stdout().replace(output_alussa, '', 1)
        output = [l for l in output_all.split("\n") if len(l)>0 ]
        
        correct = """Ato Hellas 42 vuotta (karate)
Lea Kutvonen 52 vuotta (juoksu, kamppailulajit)
Leevi Hellas 4 vuotta (palapelit)"""

        cLines = correct.split('\n')
        self.assertTrue(len(output_all)>0, f'Kun suoritetaan {koodi}, ei tulostettu mitään')
        self.assertEqual(len(cLines),len(output), f'Kun suoritetaan {koodi}, pitäisi tulostaa {len(cLines)} riviä. Tulostettiin {len(output)} riviä:\n{f(output)}')
        for rivi in cLines:
            self.assertTrue(rivi in output, f'Kun suoritetaan {koodi}, pitäisi tulostuksesta löytyä rivi\n{rivi}\nTulostettiin\n{f(output)}')         
        for rivi in output:
            self.assertTrue(rivi in correct, f'Kun suoritetaan {koodi}, sisälsi tulostus seuraavan rivin\n{rivi}\nOikea tulostus sisältää vaan seuraavat rivit\n{f(correct)}')         

    def test_2_toimii_tiedostolla3(self):
        from src.jsontiedostot import tulosta_henkilot
        output_alussa = get_stdout()
        tulosta_henkilot("tiedosto3.json")
        koodi = 'tulosta_henkilot("tiedosto3.json")'
        output_all = get_stdout().replace(output_alussa, '', 1)
        output = [l for l in output_all.split("\n") if len(l)>0 ]
        
        correct = """Matti Virtanen 78 vuotta (lukeminen, juoksu)
Antti Laaksonen 32 vuotta (algoritmit, alttoviulu)
Venla Ruuska 8 vuotta (parkour, koripallo)
Eero Luukkainen 8 vuotta (jalkapallo, lentokoneet)
Liisa Moilanen 46 vuotta (ohjelmointi, penkkiurheilu)"""

        cLines = correct.split('\n')
        self.assertTrue(len(output_all)>0, f'Kun suoritetaan {koodi}, ei tulostettu mitään')
        self.assertEqual(len(cLines),len(output), f'Kun suoritetaan {koodi}, pitäisi tulostaa {len(cLines)} riviä. Tulostettiin {len(output)} riviä:\n{f(output)}')
        for rivi in cLines:
            self.assertTrue(rivi in output, f'Kun suoritetaan {koodi}, pitäisi tulostuksesta löytyä rivi\n{rivi}\nTulostettiin\n{f(output)}')         
        for rivi in output:
            self.assertTrue(rivi in correct, f'Kun suoritetaan {koodi}, sisälsi tulostus seuraavan rivin\n{rivi}\nOikea tulostus sisältää vaan seuraavat rivit\n{f(correct)}')         

    def test_2_toimii_tiedostolla4(self):
        from src.jsontiedostot import tulosta_henkilot
        output_alussa = get_stdout()
        tulosta_henkilot("tiedosto4.json")
        koodi = 'tulosta_henkilot("tiedosto4.json")'
        output_all = get_stdout().replace(output_alussa, '', 1)
        output = [l for l in output_all.split("\n") if len(l)>0 ]
        
        correct = """Jane Doe 100 vuotta ()
Sanna Marin 38 vuotta (historia, politiikka)
Janja Garnbret 21 vuotta (boulderointi, kalliokiipeily)
Adam Ondra 28 vuotta (boulderointi, kalliokiipeily)
Barack Obama 62 vuotta (politiikka, musiikki)
Elisabeth Rehn 78 vuotta (maanpuolustus, musiikki)"""

        cLines = correct.split('\n')
        self.assertTrue(len(output_all)>0, f'Kun suoritetaan {koodi}, ei tulostettu mitään')
        self.assertEqual(len(cLines),len(output), f'Kun suoritetaan {koodi}, pitäisi tulostaa {len(cLines)} riviä. Tulostettiin {len(output)} riviä:\n{f(output)}')
        for rivi in cLines:
            self.assertTrue(rivi in output, f'Kun suoritetaan {koodi}, pitäisi tulostuksesta löytyä rivi\n{rivi}\nTulostettiin\n{f(output)}')         
        for rivi in output:
            self.assertTrue(rivi in correct, f'Kun suoritetaan {koodi}, sisälsi tulostus seuraavan rivin\n{rivi}\nOikea tulostus sisältää vaan seuraavat rivit\n{f(correct)}')         


if __name__ == '__main__':
    unittest.main()
