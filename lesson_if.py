# balance = 100
# price = 30 
# in_stock = 10

# print(bool(balance > price))  # проверка на булево 
# print(bool(in_stock))    # проверка на булево 

# if balance > price and in_stock:
#     print('Одобряем покупку')
# elif not in_stock:
#     print('Товара нету на складе')
# else:
#     print('Пожалуйста, пополните баланс!')

# def check_weather(temperature):
#     if temperature < 0:
#         return 'На улице холодно'
#     elif temperature >= 0 and temperature <=15:
#         return 'На улице прохладно'
#     elif temperature >=15 and temperature <= 20:
#         return 'На улице тепло'
#     elif temperature > 20:
#         return 'На улице жарка'


# print(check_weather(-10)) # На улице холодно
# print(check_weather(8)) # На улице прохладно
# print(check_weather(20)) # На улице тепло
# print(check_weather(25)) # На улице жарка

# def discounted(price, discount, max_discount=30, phone_name=''):
#     price = abs(price)
#     discount = abs(discount)
#     max_discount = abs(max_discount)
#     if max_discount >= 100:
#         raise ValueError("Слишком большая максимальная скидка")
#     if discount >= max_discount:
#         return price
#     elif 'iPhone' in phone_name.lower() or not phone_name: # or 'iPhone' in phone_name.lower(приводим к нижнему регистру) or not phone_name (если нету имени телефона) проверяем вхождентия в строку
#         return price
#     else:
#         return price - (price * discount / 100)

# new_price = discounted(100000, 10, phone_name='iPhone 12')
# print(new_price)

# new_price = discounted(40000, 20, phone_name='Samsung')
# print(new_price)

# new_price = discounted(5000, 20,)
# print(new_price)

# Домашнее задание №1
# Условный оператор: Возраст
# * Попросить пользователя ввести возраст при помощи input и положить 
#   результат в переменную
# * Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
#   учиться в детском саду, школе, ВУЗе или работать
# * Вызвать функцию, передав ей возраст пользователя и положить результат 
#   работы функции в переменную
# * Вывести содержимое переменной на экран
# """


# def main ():
#     age = int(input('Введите ваш возраст!: ' ))
#     if age <= 6:
#         print('идите в садик') 
#     elif 6 < age <= 18:
#         print('Идите в школу')
#     elif 19 <= age < 27:
#         print('вы должны учиться  в ВУЗЕ')
#     else:
#         print('Все прощелкал')
        
# # main()
# if __name__ == '__main__':
#     main()


# Домашнее задание №1
# Условный оператор: Сравнение строк
# * Написать функцию, которая принимает на вход две строки
# * Проверить, является ли то, что передано функции, строками. 
#   Если нет - вернуть 0
# * Если строки одинаковые, вернуть 1
# * Если строки разные и первая длиннее, вернуть 2
# * Если строки разные и вторая строка 'learn', возвращает 3
# * Вызвать функцию несколько раз, передавая ей разные праметры 
#   и выводя на экран результаты

# number_one = input('В видите слово : ')
# number_two = input('В Видите второе слово : ')

# def comparison(number_one, number_two):
#     if type(number_one) and type(number_two) is not str:
#         print(0)
#     elif number_one == number_two:
#         print(1)
#     elif number_one != number_two and len(number_one) > len(number_two):
#         print(2)
#     elif number_one != number_two and number_two == 'Learn':
#         print(3)

# comparison(number_one, number_two)

line1 = input()
line2 = input()
def lines(line1, line2):
    if isinstance(line2, str) and isinstance(line1, str):   # не работает данный цикл
        print(0)
    elif line1 == line2:
        print(1)
    elif line1 != line2 and len(line1) > len(line2):
        print(2)
    elif line1 != line2 and line2 == 'learn':
        print(3)

lines(line1, line2)
