import random


def cut_cake(people):
    try:   # для перехвата искючений пишем блок try except
        parts = 1 / people
        print(f'Каждый человек получит {parts} кусков')
    except ZeroDivisionError:
        print(f'Не могу делить на 0')
    except TypeError:
        print(f'программа принимает число')


# cut_cake('5')

while True:
    parts = random.randint(1, 10)
    cut_cake(parts)