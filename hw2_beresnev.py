 # Вариант №1 с использованием словаря
w = input('введите строку: ')
liist = dict(set(w.split()))
print(liist)

# Вариант №2 с использованием списка и цикла
w = input('введите строку: ')
liist = list(set(w.split()))
for i in range(len(liist)):
    print(liist[i], end = ' ')
