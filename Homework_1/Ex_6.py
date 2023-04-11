# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
#           Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме
#           последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
#           Вам требуется написать программу, которая проверяет счастливость билета.
#           385916 -> yes
#           123456 -> no

ticket_num = input('Введите номер билета: ')


def count_summ_digits(number):
    summ_digits = 0
    while number // 10 != 0:
        summ_digits += number % 10
        number //= 10
    summ_digits += number
    return summ_digits


def check_conditions(number):
    condition = True
    if not number.isdigit():
        condition = False
    if len(number) != 6:
        condition = False
    return condition


if check_conditions(ticket_num):
    first_part_summ = count_summ_digits(int(ticket_num[:3]))
    second_part_summ = count_summ_digits(int(ticket_num[3:]))
    print('YES' if first_part_summ == second_part_summ else 'NO')
