import random
import numpy as np
from loto_func import make_card, print_card, check_card

step = 1
while step:
    print('ИГРА "ЛОТО"')
    print('Определимся с количеством игроков')
    try:
        num_comp = int(input('Введите количество играющих компьютеров (COMP): '))
    except:
        print('Неверный ввод')
        print('Работа программы завешена')
        break
    try:
        num_human = int(input('Введите количество играющих человек (HUMAN): '))
    except:
        print('Неверный ввод')
        print('Работа программы завешена')
        break
    print(f'Всего игроков в игре: {num_comp + num_human}')

    if num_comp == 0 and num_human == 0:
        print('Играть то некому!!!')
        print('Работа программы завешена')
        break

    if (num_comp + num_human) <= 0 or num_comp < 0 or num_human < 0:
        print('Введены некорректные данные по количеству игроков')
        print('Работа программы завешена')
        break

    # Формируем карточки для всех игроков (компьютеров и людей)
    card = {}
    for n in range(num_comp):
        player = f'comp{n + 1}'
        card[player] = make_card()
    for m in range(num_human):
        player = f'human{m + 1}'
        card[player] = make_card()
    print('Игроки получили свои карточки ')
    for key in card:
        print_card(card[key], key)

    # Формируем мешок с бочонками и перемешиваем его
    bag = np.array(range(1, 91))
    random.shuffle(bag)

    # Ничинаем играть
    while step:
        barrel = bag[0]         # Извлекаем бочонок с номером
        bag = np.delete(bag, 0) # Удаляем бочонок из мешка
        print(f'\nНовый бочонок: {barrel} (в мешке осталось {len(bag)})')
        for key in card:        # Проверяем номер и отмечаем в карточках
            if 'comp' in key:   # Карточки компьютеров проверяем автоматически и выводим проверенные на экран
                card[key] = check_card(card[key], barrel)
                print_card(card[key], key)
            if 'human' in key:  # Карточки людей проверяем после ответов на вопросы
                stroka = input(f'{key.upper()} Есть ли номер бочонка в Вашей карточке? (y/n) ')
                if stroka == 'y':
                    if barrel in card[key]:
                        card[key] = check_card(card[key], barrel)
                        print_card(card[key], key)
                    else:
                        print('Ответ неверный. Номера на карточке нет. Игра завершена.')
                        step = 0
                if stroka == 'n':
                    if barrel in card[key]:
                        print('Ответ неверный. Номер на карточке есть. Игра завершена.')
                        step = 0
                    else:
                        print_card(card[key], key)
        for key in card:        # Проверяем - все ли числа отмечены в карточках
            if card[key].max() <= 0:
                print(f'Выиграл {key.upper()}. Игра завершена.')
                step = 0
    print(f'В мешке остались бочонки:\n{bag}')
