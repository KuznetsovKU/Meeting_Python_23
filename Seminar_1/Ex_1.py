# 1. За день машина проезжает N километров. Сколько дней ей нужно, чтобы проехать маршрут длиной M километров?
#    При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

from math import ceil

car_limit = int(input('Введите максимальный суточный пробег автомобиля: '))
road_length = int(input('Введите протяженность маршрута: '))

day_counter = (car_limit + road_length - 0.1) // car_limit
print(f'Количество дней в пути: {int(day_counter)}')

day_counter_1 = ceil(road_length / car_limit)
print(f'Количество дней в пути: {int(day_counter_1)}')
