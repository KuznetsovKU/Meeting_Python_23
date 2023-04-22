# Задача №35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
#             Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
#        Input: 5
#        Output: yes

from math import sqrt


def is_simple(number):
    if number == 1:
        return f"Число {number} не является простым"
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            flag = False
            return f"Число {number} не является простым"
    return f"Число {number} является простым"


is_simple(int(input('Введите число: ')))
