w = input('введите строку: ').split()
w2 = []
for i in range(len(w)):
    if w[i] not in w2:
        w2.append(w[i])
print(*w2)

