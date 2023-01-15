from class_loto import Card


class TestCard:

    def setup(self):
        self.cards = Card()

    def test_init(self):
        for i in range(3):
            assert len(self.cards.image[i]) == 9
            result = [val for val in self.cards.image[i] if val > 0]
            assert len(result) == 5

    def test_creplace(self):
        assert self.cards.cmax() == False
        for i in range(3):
            for j in range(9):
                if self.cards.image[i, j] > 0:
                    self.cards.image[i, j] = -1
        assert self.cards.cmax() == True

    def test_cmax(self):
        assert self.cards.cmax() == False

    def test_isnum(self):
        for i in range(3):
            for j in range(9):
                if self.cards.image[i, j] <= 0:
                    assert self.cards.isnum(0) == True
                else:
                    numb = self.cards.image[i, j]
                    assert self.cards.isnum(numb) == True
