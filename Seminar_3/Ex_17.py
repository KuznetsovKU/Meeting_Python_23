# Задача 17. Дан список чисел. Определите, сколько в нем встречается различных чисел

numbers = [1, 2, 2, 24, 5, 5, 8, 8, 9]
unique_numbers = set(numbers)
print(f'Количество уникальных чисел в списке: {len(unique_numbers)}')