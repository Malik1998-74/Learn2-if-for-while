# for namber in range(3):
#     print(f'номер {namber}')

# for letter in 'python':
#     print(letter.upper())

# my_string = 'привет я учу python'

# for word in my_string.split():  # сплит это разделение по словам
#     print(f'Длинна слова {word}; {len(word)}') # ф строка переменные пишуться в фигурных скобках

# students_scores = [3, 5, 4, 4, 2 ]

# avg_score = 0

# for score in students_scores:
#     avg_score = avg_score + score
    
# class_avg = avg_score / len(students_scores)
# print(class_avg)

# stock = [
# 		{'name': 'iPhone 12', 'stock': 24, 'price': 65432.1,
#                 'discount': 25},
# 		{'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0,
#                 'discount': 10},
# 		{'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10}
# ]
			
# def discounted(price, discount, max_discount=30, phone_name=''):
#     price = abs(price)  #  привеодим в абсолютное значение чтобы число было положительным а не отрицательным
#     discount = abs(discount)
#     max_discount = abs(max_discount)
#     if max_discount >= 100:  # если максимальная скидка больше или равна 100 то срабатывает ошибка(слишком большая скидка) 
#         raise ValueError("Слишком большая максимальная скидка")
#     if discount >= max_discount: # если скидка больше или равна максимальной скидке то возвращаем цену без скидки
#         return price
#     elif 'iphone' in phone_name.lower() or not phone_name: # or 'iPhone' in phone_name.lower(приводим к нижнему регистру) or not phone_name (если нету имени телефона) проверяем вхождентия в строку
#         return price
#     else:
#         return price - (price * discount / 100)

# for phone in stock: # делаем цикл чтобы пробежала по stock передаем в функцию discounted цену телефона скидку телефона имя телефона
#     phone['price_final'] = discounted(phone['price'], phone['discount'], phone_name=phone['name'])

# print(stock)


classes = [
    {'name': '3А', 'scores': [3,4,4,5,2]},
    {'name': '3Б', 'scores': [5,5,3,2,2]},
    {'name': '3В', 'scores': [4,5,3,5,4]},
]

def count_class_avg(student_scores):
    scores_sum = 0
    for score in student_scores:
        scores_sum += score
    return scores_sum / len(student_scores)

school_avg_sum = 0
for one_class in classes:
    class_avg = count_class_avg(one_class['scores'])
    print(f'Средняя оценка класса {one_class["name"]}: {class_avg}')
    school_avg_sum += class_avg

scool_avg = round(school_avg_sum / len(classes), 2)
# print(f'Средняя оценка школы {school_avg_sum / len(classes)}')
print(f'Средняя оценка по школе {scool_avg}')