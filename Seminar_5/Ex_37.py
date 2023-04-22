# Задача №37. Дано натуральное число N и последовательность из N элементов.
#             Требуется вывести эту последовательность в обратном порядке.
#             Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
#       Input: 2 -> 3 4
#       Output: 4 3

amount = int(input('Введите количество элементов: '))


# def fill_sequence(elements_amount):
#     line = ''
#     if elements_amount == 1:
#         line += input('Введите очередной элемент последовательности: ')
#         return line
#     else:
#         return fill_sequence(elements_amount - 1) + input('Введите очередной элемент последовательности: ')
#
#
# def reverse_line(input_line):
#     output_line = ''
#     if len(input_line) == 1:
#         output_line += input_line[-1]
#         return output_line
#     else:
#         return input_line[-1] + reverse_line(input_line[:-1])

# sequence_line = fill_sequence(amount)
# sequence_line_revere = reverse_line(sequence_line)
# print(' '.join(sequence_line_revere))


def fill_sequence(elements_amount):
    if elements_amount == 0:
        return "!"
    line = input('Введите очередной элемент последовательности: ')
    return str(fill_sequence(elements_amount - 1)) + " " + line


print(fill_sequence(amount))

