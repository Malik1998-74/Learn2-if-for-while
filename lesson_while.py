# x = 1
# while x < 5:
#     print(x)
#     x += 1

while True:  # бесконечный цикл
    user_say = input('Скажи что-нибудь: ')  # input просим ввести
    if user_say == 'Пока': # пока пользователь не введет слово пока цикл будет продолжаться 
        print('Ну пока')
        break  # остановка цикла 
    else:
        print('Сам ты {}'.format(user_say))
        

