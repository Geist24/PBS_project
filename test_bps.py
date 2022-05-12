import unittest
import bps


class MyTestCase(unittest.TestCase):
    def test_comp_choice(self):
        bps.random.seed(1)
        self.assertEqual(bps.comp_choice(), 'Boulder')  # add assertion here

    def test_logic(self):
        self.assertEqual(bps.logic('boulder', 'boulder'), 4)
        self.assertEqual(bps.logic('parchment', 'parchment'), 4)
        self.assertEqual(bps.logic('shears', 'shears'), 4)

        self.assertEqual(bps.logic('boulder', 'parchment'), 5)
        self.assertEqual(bps.logic('boulder', 'shears'), 6)

        self.assertEqual(bps.logic('parchment', 'boulder'), 6)
        self.assertEqual(bps.logic('parchment', 'shears'), 5)

        self.assertEqual(bps.logic('shears', 'boulder'), 5)
        self.assertEqual(bps.logic('shears', 'parchment'), 6)


if __name__ == '__main__':
    unittest.main()
