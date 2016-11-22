# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, dragon_list):
    for dragon in dragon_list:
        print('тебе покушать принес', dragon._color, 'дракон!')
        while dragon.is_alive() and hero.is_alive():
            print('Очень сложное вычисление:', dragon.question())
            answer = annoying_input_int('Отвечай бро:')

            if dragon.check_answer(answer):
                hero.attack(dragon)
                print('Верно! \n** дракон орет с твоих мемов **')
            else:
                dragon.attack(hero)
                print('Ну ты и тупой! \n** дракон шлет тебе баяны... **')
        if dragon.is_alive():
            break
        print('Дракон', dragon._color, 'считает тебя братишкой!\n')
        hero._experience += 50
        print('Вы получаете 50 опыта')
        hero.level_up()

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш уровень:', hero._level, 'Ваш накопленный опыт:', hero._experience + (hero._level - 1) * 150)
    else:
        print('К сожалению, Вы проиграли...')

def start_game():

    try:
        print('!000000    111111      22        33333        444      5      5    66666 !')
        print('10     0   1    11    2  2      3     3     44   44    55     5  6      6!')
        print('!0      0  1    11   2    2    3       3   4       4   5 5    5  6       !')
        print('!0      0  1    11  2      2  3           4         4  5  5   5   666    !')
        print('!0      0  111111   2      2  3           4         4  5   5  5      666 !')
        print('!0      0  11       22222222  3     3333  4         4  5    5 5         6!')
        print('!0      0  1 11     2      2  3        3   4       4   5     55         6!')
        print('!0     0   1   11   2      2   3      3     44   44    5      5  6      6!')
        print('!000000    1    11  2      2    333333        444      5      5   666666 !')
        print('Добро пожаловать в непонятную фигню!')
        print('Представься браптишка: ', end = '')
        
        hero = Hero(input())

        dragon_number = randint(1,5)
        dragon_list = generate_dragon_list(dragon_number)
        assert(len(dragon_list) == dragon_number)
        print('У Вас на пути', dragon_number, 'драконов!')
        game_tournament(hero, dragon_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
