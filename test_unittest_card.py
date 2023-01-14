import unittest
from class_loto import Card


class TestCard(unittest.TestCase):

    def setUp(self):
        self.cards = Card()

    def test_init(self):
        for i in range(3):
            self.assertEqual(len(self.cards.image[i]), 9)
            result = [val for val in self.cards.image[i] if val > 0]
            self.assertEqual(len(result), 5)

    def test_creplace(self):
        self.assertFalse(self.cards.cmax())
        for i in range(3):
            for j in range(9):
                if self.cards.image[i, j] > 0:
                    self.cards.image[i, j] = -1
        self.assertTrue(self.cards.cmax())

    def test_cmax(self):
        self.assertFalse(self.cards.cmax())

    def test_isnum(self):
        for i in range(3):
            for j in range(9):
                if self.cards.image[i, j] <= 0:
                    self.assertTrue(self.cards.isnum(0))
                else:
                    numb = self.cards.image[i, j]
                    self.assertTrue(self.cards.isnum(numb))


