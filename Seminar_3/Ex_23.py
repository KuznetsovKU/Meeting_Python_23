# Задача 23. Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива,
#            больших предыдущего (элемента с предыдущим номером)
#     Input: [0, -1, 5, 2, 3]
#     Output: 2 (-1 < 5, 2 < 3)

input_array = [0, -1, 5, 2, 3]
counter = 0

for i in range(1, len(input_array)):
    if input_array[i] > input_array[i - 1]:
        counter += 1

print(counter)
