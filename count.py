from collections import Counter # тип данных Counter из модуля Collections позволит нам легко подсчитать количество элементов в списке или букв в слове.

phones = ['iPhone', 'Samsung', 'LG', 'iPhone', 'LG']  
count = Counter(phones)
print(count)

# print(count['LG'])  # обращение только к одному элементу в списке
# print(count)  # обращение ко всем элементам в списке

text = 'ЕхалS грека через реку'
count = Counter(text.lower().replace(' ',''))  # .lower() переводим все к нижнему регистру затем  .replace(' ', '') заменяем пробел 
print(count)