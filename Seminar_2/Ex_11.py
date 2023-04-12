# Задача 11. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
#            выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1

a = int(input('Введите натуральное число (больше 1): '))

fibo_start_counter = 0
fibo_end_counter = 1
fibo_position_counter = 2
while fibo_end_counter < a:
    fibo_current_num = fibo_start_counter + fibo_end_counter
    fibo_start_counter = fibo_end_counter
    fibo_end_counter = fibo_current_num
    fibo_position_counter += 1
if fibo_end_counter == a:
    print(f'Число {a} является {fibo_position_counter} по счету числом Фибоначчи')
else:
    print(-1)
