import unittest

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.seitseman_veljesta'
@points('1.seitseman_veljesta')
class SeitsemanVeljestaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'fi')

    def test_content(self):
        reload_module(self.module)
        split_output = get_stdout().split('\n')
        self.assertEqual(len(split_output), 7, 'Tulostuksessa odotettiin olevan {0} riviä, ohjelmasi tulostaa tällä hetkellä {1} riviä.'.format(7, len(split_output)))
        correct = "Aapo Eero Juhani Lauri Simeoni Timo Tuomas".split()
        for i in range(7):
            self.assertEqual(split_output[i], correct[i], "Rivin {0} tulostus väärin.".format(i + 1))

if __name__ == '__main__':
    unittest.main()
    