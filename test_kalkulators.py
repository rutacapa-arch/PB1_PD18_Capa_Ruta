import unittest
from kalkulators import saskaitit

class TestKalkulators(unittest.TestCase):
    def test_saskaitit_pozitivus_skaitlus(self):
        self.assertEqual(saskaitit(2, 3), 5) 
    def test_saskaitit_negativus_skaitlus(self):
        self.assertEqual(saskaitit(-2, -3), -5)
    def test_saskaitit_ar_nulli(self):
        self.assertEqual(saskaitit(0, 7), 7)
    def test_saskaitit_jauktas_zimes(self):
        self.assertEqual(saskaitit(-5, 5), 0)

if __name__ == "__main__":
    unittest.main()
