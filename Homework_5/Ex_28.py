# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
#            Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#            2 2
#            4

num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))

# def count_sum(first_number, second_number):
#     if second_number == 1:
#         return first_number + 1
#     else:
#         return count_sum(first_number, second_number - 1) + 1


def count_sum(first_number, second_number):
    if first_number == 0:
        return second_number
    elif second_number == 0:
        return first_number
    elif first_number == 1 and second_number == 1:
        return 1 + 1
    elif first_number == 1:
        return count_sum(first_number, second_number - 1) + 1
    elif second_number == 1:
        return count_sum(first_number - 1, second_number) + 1
    else:
        return count_sum(first_number - 1, 1) + count_sum(1, second_number - 1)


print(count_sum(num_1, num_2))
