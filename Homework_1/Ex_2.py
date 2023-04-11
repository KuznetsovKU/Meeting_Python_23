# Задача 2: Найдите сумму цифр трехзначного числа.
#           123 -> 6 (1 + 2 + 3)
#           100 -> 1 (1 + 0 + 0)

num = input('Введите трехзначное число: ')


def is_number(input_value):
    condition_check = True
    if input_value[0] == '-':
        input_value = input_value[1:]
    if len(input_value) != 3:
        condition_check = False
    if not input_value.isdigit():
        condition_check = False
    return condition_check


def count_sum_by_slices(input_value):
    if is_number(input_value):
        summ_digits = int(input_value[0]) + int(input_value[1]) + int(input_value[2])
        print(f'Сумма цифр по срезам строки равна: {summ_digits}')
    else:
        print('Введите корректные данные!')


def count_sum_by_int_type(input_value):
    if is_number(input_value):
        number = int(input_value)
        summ_digits = 0
        while number > 0:
            summ_digits += number % 10
            number //= 10
        print(f'Сумма цифр по int равна: {summ_digits}')
    else:
        print('Введите корректные данные!')


count_sum_by_slices(num)
count_sum_by_int_type(num)
