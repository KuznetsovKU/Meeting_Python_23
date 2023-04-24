# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B
#            с помощью рекурсии.
#            A = 3; B = 5 -> 243 (3⁵)
#            A = 2; B = 3 -> 8

number = int(input('Введите число: '))
grade = int(input('Введите степень: '))


def count_degree(input_number, input_grade):
    result = 1
    if input_grade == 0:
        return result
    elif input_grade > 0:
        if input_grade == 1:
            return result * input_number
        else:
            return input_number * count_degree(input_number, input_grade - 1)
    else:
        return 1 / count_degree(input_number, input_grade * -1)


print(count_degree(number, grade))
