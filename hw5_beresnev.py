# Запрашиваем ввод данных
nums = input('Введите в строку положительные целые числа: ').split()

# Переносим из списка со строками в список с числами
newnums = [int(num) for num in nums]

# Сортируем список по возрастанию
newnums.sort()

# Инициируем переменную, в которой будем хранить "потерянное число", минимальное положительное,
# не указанное пользователем
lostnum = 0

# Ищем перебором пропуск во введенном пользователем списке , если пропуска нет,
# то записываем значение последнего числа в списке
for n in range(1, len(newnums)):
    if newnums[n] - newnums[n - 1] == 1:
        lostnum = newnums[n]
    elif newnums[n] - newnums[n - 1] > 1:
        lostnum = newnums[n-1]+1
        break

# Проверяем выходит ли наименьшее неуказанное число за границы списка, тогда выбираем его до или после списка
if newnums[0] > 1 and 1 not in newnums:
    lostnum = 1
elif lostnum == newnums[-1]:
    lostnum = newnums[-1]+1
# Выводим "потеряшку"
print(lostnum)
