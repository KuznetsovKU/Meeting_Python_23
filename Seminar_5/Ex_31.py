# Задача №31. Последовательностью Фибоначчи называется последовательность чисел a0 , a1 , ..., an , ..., где
#             a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
#       Input: 7
#       Output: 21
#       Задание необходимо решать через рекурсию

requested_num = int(input('Введите порядковый номер числа в последовательности Фибоначчи: '))


def find_fibo(number):
    if number in (0, 1):  # == 0 or number == 1:
        return number
    else:
        return find_fibo(number - 1) + find_fibo(number - 2)


def fill_fibo_array(number):
    output_array = []
    for i in range(number + 1):  # т.к. считаем, что 0 - это НУЛЕВОЙ элемент
        output_array.append(find_fibo(i))
    return output_array


fibo_array = fill_fibo_array(requested_num)
print(*fibo_array)
print(f'Числом с порядковым номером {requested_num} в последовательности Фибоначчи является число '
      f'{find_fibo(requested_num)}')
