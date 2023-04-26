# Задача №41. Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит
#             количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного.
#             Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива.
#             Массив состоит из целых чисел.

def fill_array(size):
    output_array = []
    for _ in range(size):
        output_array.append(int(input('Введите очередной элемент массива: ')))
    return output_array


array_1_size = int(input('Введите количество элементов массива: '))
array_1 = fill_array(array_1_size)
counter = 0

for i in range(1, array_1_size - 1):
    if array_1[i] > array_1[i - 1] and array_1[i] > array_1[i + 1]:
        counter += 1

print(counter)
