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

def discounted(price, discount, max_discount=30, phone_name=''):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError("Слишком большая максимальная скидка")
    if discount >= max_discount:
        return price
    elif 'iPhone' in phone_name.lower() or not phone_name: # or 'iPhone' in phone_name.lower(приводим к нижнему регистру) or not phone_name (если нету имени телефона) проверяем вхождентия в строку
        return price
    else:
        return price - (price * discount / 100)

new_price = discounted(100000, 10, phone_name='iPhone 12')
print(new_price)

new_price = discounted(40000, 20, phone_name='Samsung')
print(new_price)

new_price = discounted(5000, 20,)
print(new_price)