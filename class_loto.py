import numpy as np
import random


class Card:

    def __init__(self):
        a = [1, 10, 20, 30, 40, 50, 60, 70, 80]
        b = [10, 20, 30, 40, 50, 60, 70, 80, 91]
        card_start = np.zeros((3, 9), dtype=int)
        for i in range(9):
            array_start = np.array(range(a[i], b[i]))
            random.shuffle(array_start)
            new_list = array_start[:3]
            for j in range(3):
                card_start[j, i] = new_list[j]
        # Создадим маску по пять чисел в каждой строке
        mask = np.zeros((3, 9), dtype=int)
        array_mask = np.array(range(9))
        random.shuffle(array_mask)
        new_array = array_mask[:5]
        for i in new_array:
            mask[0, i] = 1
        for i in range(9):
            mask[2, i] = not mask[0, i]
        f = random.choice(new_array)
        mask[2, f] = 1
        array_end = np.array(range(9))
        array_end_f = np.delete(array_end, f)
        random.shuffle(array_end_f)
        new_array = array_end_f[:5]
        for i in new_array:
            mask[1, i] = 1
        # Формируем карточку
        card_end = np.zeros((3, 9), dtype=int)
        for i in range(3):
            for j in range(9):
                if mask[i, j]:
                    card_end[i, j] = card_start[i, j]

        self.image = card_end

    def cprint(self, player):
        """
        Выводим на экран карточку конкретного игрока
        :param player:
        :return:
        """
        print(f'---Карточка игрока {player.upper()}---')
        for i in range(3):
            for j in range(9):
                if self.image[i, j]:
                    if j == 0:
                        print(' ', end=' ')
                    if self.image[i, j] == -1:
                        if j == 0:
                            print('*', end=' ')
                        else:
                            print('**', end=' ')
                    else:
                        print(str(self.image[i, j]), end=' ')
                else:
                    if j == 0:
                        print('', end=' ')
                    print('  ', end=' ')
            print()
        print('-' * 29)

    def creplace(self, num):
        """
        Вместо номера в карточке записываем (-1)
        :param num:
        :return:
        """
        for i in range(3):
            for j in range(9):
                if self.image[i, j] == num:
                    self.image[i, j] = -1

    def cmax(self):
        """
        Проверяем что максимальное значение числа в карточке не больше нуля
        :return:
        """
        return self.image.max() <= 0

    def isnum(self, numb):
        """
        Проверяем, есть ли выпавший номер (num) в карточке игрока.
        :param num:
        :return:
        """
        return numb in self.image


if __name__ == '__main__':
    crd = Card()
    player = "TEST"
    crd.cprint(player)
    num = random.choice(range(1, 91))
    print(num)
    crd.creplace(num)
    crd.cprint(player)
    print(crd.cmax())
    print(crd.isnum(num))
