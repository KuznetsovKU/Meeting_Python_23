# Задача 18: Требуется найти в массиве A самый близкий по величине элемент к заданному числу X. Если таких элементов
#            несколько, вы вывести один любой. Пользователь в первой строке вводит натуральное число N – количество
#            элементов в массиве. В последующих строках записаны N целых чисел Ai (можно использовать псевдогенерацию).
#            Последняя строка содержит число X
#
#            5
#            7 -2 3 5 1
#            6
#            -> 7

elements_amount = int(input("Введите количество элементов массива: "))
array = []
for _ in range(elements_amount):
    array.append(int(input('Введите очередной элемент массива (число): ')))

requested_value = int(input('Введите искомое число: '))
min_difference = abs(requested_value - array[0])
current_element = array[0]

for i in range(len(array)):
    if abs(requested_value - array[i]) < min_difference:
        min_difference = abs(requested_value - array[i])
        current_element = array[i]

print(f'Самый близкий к {requested_value} по значению элемент: {current_element}')
