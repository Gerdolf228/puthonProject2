import random
n = int(input("Введите кол-во строк матрицы: "))
m = int(input("Введите кол-во столбцов матрицы: "))
listA = []
for i in range(n):
    listB = [random.randint(-100, 100) for x in range(m)]
    listA.append(listB)
for i in listA:
    print(i)
P = 0
for i in range(n):
    for j in range(n):
        if i == j:
            if P < listA[i][j]:
                P = listA[i][j]
print('Наибольшее значение диагонали = ', P)