# Задача №33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
#             максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные –
#             на минимальные.
#       Input: 5 -> 1 3 3 3 4
#       Output: 1 3 3 3 1

points_amount = int(input('Введите количество оценок в журнале: '))


def fill_points_array(count):
    output_array = []
    for i in range(count):
        output_array.append(int(input('Введите оценку ученика: ')))
    return output_array


def change_points(input_array):
    max_score = max(input_array)
    min_score = min(input_array)
    if max_score != min_score:
        for i in range(len(input_array)):
            if input_array[i] == max_score:
                input_array[i] = min_score
    return input_array


points_array = fill_points_array(points_amount)
print(points_array)
print(change_points(points_array))
