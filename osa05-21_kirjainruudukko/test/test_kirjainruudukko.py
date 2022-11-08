import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
import os

exercise = 'src.kirjainruudukko'

@points('3.kirjainruudukko')
class RuudukkoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[1] + ["2"] * 10):
           cls.module = load_module(exercise, 'fi')

    def test_2(self):
        luku = 2
        with patch('builtins.input', side_effect=[str(luku), AssertionError("Syötettä pyydetään liian monta kertaa.") ], ) as prompt:
            reload_module(self.module)
            output_all =  get_stdout()
            output = output_all.split('\n')  

            expected = [
                "BBB", 
                "BAB", 
                "BBB"
            ]

            mssage = """\nHuomaa, että tässä tehtävässä mitään koodia EI TULE SIJOITTAA lohkon
if __name__ == "__main__":
sisälle
"""
            #{mssage}") 

            self.assertTrue(len(output_all)>0, f"Ohjelmasi ei tulosta mitään syötteellä {luku}\n{mssage}") 
            self.assertEqual(len(expected), len(output), f"Ohjelmasi tulisi tulostaa {len(expected)} riviä lukuja syötteellä {luku}, nyt se tulostaa {len(output)} riviä:\n{output_all}")

            for i in range(0, len(expected)):
                self.assertEqual(expected[i], output[i].strip(), f"rivin {i+1} tulostus väärin kun syöte on {luku}, rivin pitäisi olla\n{expected[i]}\ntulostit\n{output[0]}")

    def test_3(self):
        luku = 3
        with patch('builtins.input', side_effect=[str(luku), AssertionError("Syötettä pyydetään liian monta kertaa.") ], ) as prompt:
            reload_module(self.module)
            output_all =  get_stdout()
            output = output_all.split('\n')  

            expected = [
                "CCCCC", 
                "CBBBC", 
                "CBABC",
                "CBBBC",
                "CCCCC"
            ]

            self.assertTrue(len(output_all)>0, f"Ohjelmasi ei tulosta mitään syötteellä {luku}")
            self.assertEqual(len(expected), len(output), f"Ohjelmasi tulisi tulostaa {len(expected)} riviä lukuja syötteellä {luku}, nyt se tulostaa {len(output)} riviä:\n{output_all}")

            for i in range(0, len(expected)):
                self.assertEqual(expected[i], output[i].strip(), f"rivin {i+1} tulostus väärin kun syöte on {luku}, rivin pitäisi olla\n{expected[i]}\ntulostit\n{output[0]}")

        def test_4(self):
            luku = 4
            with patch('builtins.input', side_effect=[str(luku), AssertionError("Syötettä pyydetään liian monta kertaa.") ], ) as prompt:
                reload_module(self.module)
                output_all =  get_stdout()
                output = output_all.split('\n')  

                expected = [
                    "DDDDDDD"
                    "DCCCCCD", 
                    "DCBBBCD", 
                    "DCBABCD",
                    "DCBBBCD",
                    "DCCCCCD",
                    "DDDDDDD"
                ]

                self.assertTrue(len(output_all)>0, f"Ohjelmasi ei tulosta mitään syötteellä {luku}")
                self.assertEqual(len(expected), len(output), f"Ohjelmasi tulisi tulostaa {len(expected)} riviä lukuja syötteellä {luku}, nyt se tulostaa {len(output)} riviä:\n{output_all}")

                for i in range(0, len(expected)):
                    self.assertEqual(expected[i], output[i].strip(), f"rivin {i+1} tulostus väärin kun syöte on {luku}, rivin pitäisi olla\n{expected[i]}\ntulostit\n{output[0]}")


if __name__ == '__main__':
    unittest.main()
