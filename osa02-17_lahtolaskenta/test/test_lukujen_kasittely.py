import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint
from inspect import getsource

exercise = 'src.lahtolaskenta'

@points('2.lahtolaskenta')
class LahtolaskentaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'fi')

    def test_prints_right(self):
        reload_module(self.module)
        output = get_stdout()
        output_lines = output.split('\n')

        self.assertEqual(7, len(output_lines), "Ohjelman tulostamien rivien määrä on väärä")

        self.assertEqual(output_lines[0], "Lähtölaskenta!", "ensimmäinen tulostettu rivi väärin, ohjelmasi tulostaa\n"+ output)
        self.assertEqual(output_lines[1], "5", "toinen tulostettu rivi väärin\n"+ output)
        self.assertEqual(output_lines[2], "4", "kolmas tulostettu rivi väärin\n"+ output)
        self.assertEqual(output_lines[3], "3", "neljäs tulostettu rivi väärin\n"+ output)
        self.assertEqual(output_lines[4], "2", "viides tulostettu rivi väärin\n"+ output)
        self.assertEqual(output_lines[5], "1", "kuudes tulostettu rivi väärin\n"+ output)
        self.assertEqual(output_lines[6], "Nyt!", "seitsemäs tulostettu rivi väärin\n"+ output)

    def test_prints_in_loop(self):
        source = getsource(self.module)
        p = 0
        for line in source.split("\n"):
            if line.strip().startswith("#"):
                continue
            if "print" in line:
                p += 1
        self.assertTrue(p<4, "Ohjelmakoodissasi ei saa olla kuin kolme print-komentoa!. nyt niitä on " + str(p))


if __name__ == '__main__':
    unittest.main()
