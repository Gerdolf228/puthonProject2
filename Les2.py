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
    for j in range(0, i):
        if i > j:
            if listA[i][j] < 0:
                P += 1
print('Количество отрицательных чисел ниже главной диагонали =', P)
