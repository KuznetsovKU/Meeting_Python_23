# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите
#            минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной
#            и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
#
#            5 -> 1 0 1 1 0
#            2

coin_amount = int(input('Введите количество монеток: '))
number_side_counter = 0
emblem_side_counter = 0

for i in range(coin_amount):
    current_coin_side = int(input("Введите положение монетки (1 - вверх числом, 0 - вверх гербом): "))
    if current_coin_side == 1:
        number_side_counter += 1
    elif current_coin_side == 0:
        emblem_side_counter += 1
    else:
        break

if number_side_counter + emblem_side_counter != coin_amount:
    print('При вводе / обработке данных были допущены ошибки. Повторите операцию.')
else:
    print(number_side_counter if number_side_counter <= emblem_side_counter else emblem_side_counter)
