import numpy as np
import random

def make_card():
    """
    Создаём новую карточку игрока со случайным распределением чисел от 1 до 90
    :return: карточку игрока
    """
    # Возьмем по три неповторяющиеся числа в каждом десятке от первого до девятого
    a = [1, 10, 20, 30, 40, 50, 60, 70, 80]
    b = [10, 20, 30, 40, 50, 60, 70, 80, 91]
    card_base = np.zeros((3, 9), dtype=int)
    for i in range(9):
        arr = np.array(range(a[i], b[i]))
        random.shuffle(arr)
        new_list = arr[:3]
        for j in range(3):
            card_base[j, i] = new_list[j]
    # Создадим маску по пять чисел в каждой строке
    mask = np.zeros((3, 9), dtype=int)
    ar = np.array(range(9))
    random.shuffle(ar)
    new_ar = ar[:5]
    for i in new_ar:
        mask[0, i] = 1
    for i in range(9):
        mask[2, i] = not mask[0, i]
    f = random.choice(new_ar)
    mask[2, f] = 1
    aar = np.array(range(9))
    aarr = np.delete(aar, f)
    random.shuffle(aarr)
    new_aar = aarr[:5]
    for i in new_aar:
        mask[1, i] = 1
    # Формируем карточку
    card = np.zeros((3, 9), dtype=int)
    for i in range(3):
        for j in range(9):
            if mask[i, j]:
                card[i, j] = card_base[i, j]
    return card

def print_card(card, player):
    """
    Выводим на экран карточку конкретного игрока
    :param card:
    :param player:
    :return:
    """
    print(f'---Карточка игрока {player.upper()}---')
    for i in range(3):
        for j in range(9):
            if card[i, j]:
                if j == 0: print(' ', end=' ')
                if card[i, j] == -1:
                    if j == 0:
                        print('*', end=' ')
                    else:
                        print('**', end=' ')
                else:
                    print(str(card[i, j]), end=' ')
            else:
                if j == 0: print('', end=' ')
                print('  ', end=' ')
        print()
    print('-' * 29)

def check_card(card, num):
    """
    Проверяем, есть ли выпавший номер (num) в карточке игрока.
    Если есть - закрываем число звёздочками (**)
    :param card:
    :param num:
    :return: карточку с закрытым числом
    """
    for i in range(3):
        for j in range(9):
            if card[i, j] == num:
                card[i, j] = -1
    return card

if __name__ == '__main__':
    crd = make_card()
    player = "TEST"
    print_card(crd, player)
    num = random.choice(range(1, 91))
    print(num)
    check_card(crd, num)
    print(crd)
