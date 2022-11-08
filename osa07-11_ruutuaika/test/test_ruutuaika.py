import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.ruutuaika'

def f(a):
    return "\n".join(a)

def get_content(tiedosto):
    try:
        with open(tiedosto) as f:
            return [x.replace("\n","") for x in f.readlines() if len(x.strip()) > 0]
    except:
        return None

@points('7.ruutuaika')
class RuutuaikaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["vappu.txt", "1.5.2020", "1", "30 0 5"]):
           cls.module = load_module(exercise, 'fi')
    
    def test_toiminnallisuus_1(self):
        syote = ["vappu.txt", "1.5.2020", "1", "30 0 5"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, f"Varmista että ohjelmasi toimii syötteillä:\n{f(syote)}")

            output = get_stdout()
            

            msg = 'Huomaa, että tässä ohjelmassa koodia ei tule kirjoittaa if __name__ == "main" -lohkon sisälle.'

            tiedosto = syote[0]
            try:
                content = get_content(tiedosto)
                if not content:
                    self.assertTrue(False, msg)
            except:
                self.assertTrue(False, f"Ohjelmasi tulisi kirjoittaa syötteellä:\n{f(syote)}\nraportti tiedostoon {tiedosto}")

            correct = """Ajanjakso: 01.05.2020-01.05.2020
Yht. minuutteja: 35
Keskim. minuutteja: 35.0
01.05.2020: 30/0/5"""
            cLines = correct.split('\n')

            self.assertEqual(len(content), len(cLines), f"Kun ohjelma suoritetaan syötteellä:\n{f(syote)}\ntiedostossa {tiedosto} pitäisi olla nyt {len(cLines)} riviä, niitä on kuitenkin {len(content)}\nTiedoston sisältö on:\n{f(content)}")

            for i in range(0, len(cLines)):
                r = content[i].strip()
                c = cLines[i].strip()
                self.assertEqual(r, c, f"Kun ohjelma suoritetaan syötteellä:\n{f(syote)}\ntiedostossa {tiedosto} rivin numero {i+1} pitäisi olla\n{c}\nSe kuitenkin on:\n{r}\nTiedoston koko sisältö on:\n{f(content)}")

    def test_toiminnallisuus_2(self):
        syote = ["kesakuun_alku.txt", "1.6.2020", "3", "30 0 5", "180 90 15", "0 240 25"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, f"Varmista että ohjelmasi toimii syötteellä:\n{f(syote)}")

            output = get_stdout()
            tiedosto = syote[0]
            try:
                content = get_content(tiedosto)
            except:
                self.assertTrue(False, f"Ohjelmasi tulisi kirjoittaa syötteellä:\n{f(syote)}\nraportti tiedostoon {tiedosto}")

            correct = """Ajanjakso: 01.06.2020-03.06.2020
Yht. minuutteja: 585
Keskim. minuutteja: 195.0
01.06.2020: 30/0/5
02.06.2020: 180/90/15
03.06.2020: 0/240/25"""
            cLines = correct.split('\n')

            self.assertEqual(len(content), len(cLines), f"Kun ohjelma suoritetaan syötteellä:\n{f(syote)}\ntiedostossa {tiedosto} pitäisi olla nyt {len(cLines)} riviä, niitä on kuitenkin {len(content)}\nTiedoston sisältö on:\n{f(content)}")

            for i in range(0, len(cLines)):
                r = content[i].strip()
                c = cLines[i].strip()
                self.assertEqual(r, c, f"Kun ohjelma suoritetaan syötteellä:\n{f(syote)}\ntiedostossa {tiedosto} rivin numero {i+1} pitäisi olla\n{c}\nSe kuitenkin on:\n{r}\nTiedoston koko sisältö on:\n{f(content)}")

    def test_toiminnallisuus_3(self):
        syote = ["kesakuun_loppu.txt", "29.6.2020", "4", "30 100 0", "55 40 0", "0 240 25", "180 240 100"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, f"Varmista että ohjelmasi toimii syötteellä:\n{f(syote)}")

            output = get_stdout()
            tiedosto = syote[0]
            try:
                content = get_content(tiedosto)
            except:
                self.assertTrue(False, f"Ohjelmasi tulisi kirjoittaa syötteellä:\n{f(syote)}\nraportti tiedostoon {tiedosto}")

            correct = """Ajanjakso: 29.06.2020-02.07.2020
Yht. minuutteja: 1010
Keskim. minuutteja: 252.5
29.06.2020: 30/100/0
30.06.2020: 55/40/0
01.07.2020: 0/240/25
02.07.2020: 180/240/100"""
            cLines = correct.split('\n')

            self.assertEqual(len(content), len(cLines), f"Kun ohjelma suoritetaan syötteellä:\n{f(syote)}\ntiedostossa {tiedosto} pitäisi olla nyt {len(cLines)} riviä, niitä on kuitenkin {len(content)}\nTiedoston sisältö on:\n{f(content)}")

            for i in range(0, len(cLines)):
                r = content[i].strip()
                c = cLines[i].strip()
                self.assertEqual(r, c, f"Kun ohjelma suoritetaan syötteellä:\n{f(syote)}\ntiedostossa {tiedosto} rivin numero {i+1} pitäisi olla\n{c}\nSe kuitenkin on:\n{r}\nTiedoston koko sisältö on:\n{f(content)}")

    def test_toiminnallisuus_4(self):
        syote = ["helmikuun_loppu.txt", "27.2.2020", "5", "30 15 15", "20 140 100", "10 200 35", "0 0 300", "5 5 5"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, f"Varmista että ohjelmasi toimii syötteellä:\n{f(syote)}")

            output = get_stdout()
            
            tiedosto = syote[0]
            try:
                content = get_content(tiedosto)
            except:
                self.assertTrue(False, f"Ohjelmasi tulisi kirjoittaa syötteellä:\n{f(syote)}\nraportti tiedostoon {tiedosto}")

            correct = """Ajanjakso: 27.02.2020-02.03.2020
Yht. minuutteja: 880
Keskim. minuutteja: 176.0
27.02.2020: 30/15/15
28.02.2020: 20/140/100
29.02.2020: 10/200/35
01.03.2020: 0/0/300
02.03.2020: 5/5/5"""
            cLines = correct.split('\n')

            self.assertEqual(len(content), len(cLines), f"Kun ohjelma suoritetaan syötteellä:\n{f(syote)}\ntiedostossa {tiedosto} pitäisi olla nyt {len(cLines)} riviä, niitä on kuitenkin {len(content)}\nTiedoston sisältö on:\n{f(content)}")

            for i in range(0, len(cLines)):
                r = content[i].strip()
                c = cLines[i].strip()
                self.assertEqual(r, c, f"Kun ohjelma suoritetaan syötteellä:\n{f(syote)}\ntiedostossa {tiedosto} rivin numero {i+1} pitäisi olla\n{c}\nSe kuitenkin on:\n{r}\nTiedoston koko sisältö on:\n{f(content)}")

    def test_toiminnallisuus_5(self):
        syote = ["helmikuun_loppu_2021.txt", "27.2.2021", "5", "30 15 15", "20 140 100", "10 200 35", "0 0 300", "5 5 5"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, f"Varmista että ohjelmasi toimii syötteellä:\n{f(syote)}")

            output = get_stdout()
            tiedosto = syote[0]
            try:
                content = get_content(tiedosto)
            except:
                self.assertTrue(False, f"Ohjelmasi tulisi kirjoittaa syötteellä:\n{f(syote)}\nraportti tiedostoon {tiedosto}")

            correct = """Ajanjakso: 27.02.2021-03.03.2021
Yht. minuutteja: 880
Keskim. minuutteja: 176.0
27.02.2021: 30/15/15
28.02.2021: 20/140/100
01.03.2021: 10/200/35
02.03.2021: 0/0/300
03.03.2021: 5/5/5"""
            cLines = correct.split('\n')

            self.assertEqual(len(content), len(cLines), f"Kun ohjelma suoritetaan syötteellä:\n{f(syote)}\ntiedostossa {tiedosto} pitäisi olla nyt {len(cLines)} riviä, niitä on kuitenkin {len(content)}\nTiedoston sisältö on:\n{f(content)}")

            for i in range(0, len(cLines)):
                r = content[i].strip()
                c = cLines[i].strip()
                self.assertEqual(r, c, f"Kun ohjelma suoritetaan syötteellä:\n{f(syote)}\ntiedostossa {tiedosto} rivin numero {i+1} pitäisi olla\n{c}\nSe kuitenkin on:\n{r}\nTiedoston koko sisältö on:\n{f(content)}")
    
    def test_toiminnallisuus_6(self):
        syote = ["vuodenvaihde.txt", "29.12.2020", "6", "30 15 15", "5 140 90", "0 100 35", "5 15 15",  "0 0 0",  "100 10 10"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, f"Varmista että ohjelmasi toimii syötteellä:\n{f(syote)}")

            output = get_stdout()
            
            tiedosto = syote[0]
            try:
                content = get_content(tiedosto)
            except:
                self.assertTrue(False, f"Ohjelmasi tulisi kirjoittaa syötteellä:\n{f(syote)}\nraportti tiedostoon {tiedosto}")

            correct = """Ajanjakso: 29.12.2020-03.01.2021
Yht. minuutteja: 585
Keskim. minuutteja: 97.5
29.12.2020: 30/15/15
30.12.2020: 5/140/90
31.12.2020: 0/100/35
01.01.2021: 5/15/15
02.01.2021: 0/0/0
03.01.2021: 100/10/10"""
            cLines = correct.split('\n')

            self.assertEqual(len(content), len(cLines), f"Kun ohjelma suoritetaan syötteellä:\n{f(syote)}\ntiedostossa {tiedosto} pitäisi olla nyt {len(cLines)} riviä, niitä on kuitenkin {len(content)}\nTiedoston sisältö on:\n{f(content)}")

            for i in range(0, len(cLines)):
                r = content[i].strip()
                c = cLines[i].strip()
                self.assertEqual(r, c, f"Kun ohjelma suoritetaan syötteellä:\n{f(syote)}\ntiedostossa {tiedosto} rivin numero {i+1} pitäisi olla\n{c}\nSe kuitenkin on:\n{r}\nTiedoston koko sisältö on:\n{f(content)}")


if __name__ == '__main__':
    unittest.main()
