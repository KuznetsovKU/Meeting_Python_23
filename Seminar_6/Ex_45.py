# Задача №45. Два различных натуральных числа n и m называются дружественными, если сумма делителей числа (включая 1,
#             но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу
#             k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход
#             одно натуральное число k, не превосходящее 10**5. Программа должна вывести все пары дружественных чисел,
#             каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами.
#             Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).


number = int(input('Введите число: '))


def find_div_sum(value):
    amount = 1
    for el in range(2, value // 2 + 1):
        if value % el == 0:
            amount += el
    return amount


def find_pairs(value):
    # amicable_numbers = []
    pairs_dict = {}                               # ключ словаря = сумма делителей некоего числа
    for i in range(1, value + 1):                # проходим по числам от 1 до number, включая number
        dividers_sum = find_div_sum(i)
        if dividers_sum in pairs_dict and pairs_dict[dividers_sum] == i and i != dividers_sum:
            print(i, dividers_sum)
            # amicable_numbers.append((i, dividers_sum))
        pairs_dict[i] = dividers_sum


find_pairs(number)


# for i in range(1, number + 1):                  # проходим по числам от 1 до number, включая number
#     # заполняем словарь: ключ = число от 1 до number, включая number => избегаем перезаписываний
#     pairs_dict[i] = pairs_dict.get(i, find_div_sum(i))
#
#
# result_dict = {}  # объявляем результирующий словарь
# for i in pairs_dict:                              # проходим по ключам pairs_dict
#     if i in pairs_dict.values():                  # если ключ присутствует в значениях
#         if i == find_div_sum(pairs_dict[i]):      # если ключ равен сумме делителей значения
#             if i != pairs_dict[i]:                # если ключ НЕ равен своему значению
#                 if i not in result_dict.values(): # если ключа нет в значениях результирующего словаря
#                     result_dict[i] = result_dict.get(i, pairs_dict[i])  # записываем в результирующий словарь
#                     print(i, pairs_dict[i])       # выводим пару, т.к. "дружественность" подтверждена
