# Задача №43. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые
#             два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список чисел.
#             Все числа списка находятся на разных строках.

def fill_array():
    output_array = []
    while True:
        element = (int(input('Введите очередной элемент массива: ')))
        if element != 0:
            output_array.append(element)
        else:
            break
    return output_array


array = fill_array()
pair_counter = 0
# # # for i in range(len(array)):  # решение, соответствующее условию задачи
# # #     for j in range(i + 1, len(array)):
# # #         if array[i] == array[j]:
# # #             pair_counter += 1
# #
# # frequency_dict = {}  # решение, если считать только полные пары без дублирования (3 эл = 1 пара, 4 эл = 2 пары)
# # for i in array:
# #     frequency_dict[i] = frequency_dict.get(i, 0) + 1
# # for value in frequency_dict.values():
# #     pair_counter += value // 2
#
# for i in range(1, len(array)):  # решение, если парой считать только одинаковые элементы, идущие подряд
#     if array[i] == array[i - 1]:
#         pair_counter += 1


def pair_req_counter(input_arr):
    elem, *input_arr = input_arr
    if input_arr:
        return pair_req_counter(input_arr) + input_arr.count(elem)
    return 0


arr_2 = array[:]
while arr_2:
    el, *arr_2 = arr_2
    pair_counter += arr_2.count(el)

print(pair_counter)
print(pair_req_counter(array))
