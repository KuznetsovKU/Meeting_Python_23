# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке
#            возрастания все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во
#            элементов первого множества. m - кол-во элементов второго множества.
#            Затем пользователь вводит сами элементы множеств.
#      Input: 11 6
#             2 4 6 8 10 12 10 8 6 4 2
#             3 6 9 12 15 18
#     Output: 6 12

array_1_length = int(input('Введите количество элементов первого множества: '))
array_2_length = int(input('Введите количество элементов второго множества: '))
array_1 = []
array_2 = []
array_3 = []
for _ in range(array_1_length):
    array_1.append(int(input('Введите очередной элемент первого множества: ')))
for _ in range(array_2_length):
    array_2.append(int(input('Введите очередной элемент второго множества: ')))
for i in array_1:
    if i in array_2:
        array_3.append(i)
array_3 = list(set(array_3))
array_3.sort()
print(*array_3)