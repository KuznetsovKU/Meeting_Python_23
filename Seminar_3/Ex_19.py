# Задача 19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
#            (сдвиг - циклический) на K элементов вправо, K – положительное число.
#     Input: [1, 2, 3, 4, 5] k = 3
#     Output: [4, 5, 1, 2, 3]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = int(input('Введите параметр сдвига: '))

current_move_steps = k % len(numbers)

output_list_1 = []
for i in range(len(numbers)):
    output_list_1.append(numbers[i + current_move_steps - len(numbers)])
print(output_list_1)

output_list_2 = numbers
for _ in range(current_move_steps):
    output_list_2.insert(0, output_list_2.pop())
print(output_list_2)

for _ in range(current_move_steps):
    output_list_2.insert(len(output_list_2), output_list_2.pop(0))
print(output_list_2)
