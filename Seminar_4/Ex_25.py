# Задача №25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
#             уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
#             Input: a a a b c a a d c d d
#             Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
#             Для решения данной задачи используйте функцию .split()

input_string = 'a a a b c a a d c d d'
elements_list = input_string.split()
elements_dict = {}
output_string = ''
output_list = []

# Формирование словаря без спец. методов:
# unique_elements = set(elements_list)
# for element in unique_elements:
#     counter = 0
#     for i in elements_list:
#         if i == element:
#             counter += 1
#     elements_dict[element] = counter

# Формирование словаря со спец. методом:
for element in elements_list:
    elements_dict[element] = elements_dict.get(element, 0) + 1

    # сборка строки
#     if elements_dict.get(element) > 1:
#         output_string += f'{element}_{str(elements_dict[element] - 1)} '
#     else:
#         output_string += f'{element} '
# print(output_string[:-1])

    # сборка списком
    if elements_dict.get(element) > 1:
        output_list.append(element + '_' + str(elements_dict.get(element) - 1))
    else:
        output_list.append(element)
print(' '.join(output_list))

# string = input_string.split()
# for i in range(len(string)):  # не оптимальное решение при сильном увеличении количества элементов
#     counter = 0
#     for j in range(i + 1, len(string)):
#         if string[i] == string[j]:
#             counter += 1
#             string[j] = f'{string[j]}_{counter}'
# print(*string)

text = input('Введите строку: ').split()

count = {}

for letter in text:
    if letter not in count:
        print(f'{letter}', end=' ')
    else:
        print(f'{letter}_{count[letter]}', end=" ")
    count[letter] = count.get(letter, 0) + 1
