# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать
#           один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
#           3 2 4 -> yes
#           3 2 1 -> no

choco_length = int(input('Введите длину шоколадки: '))
choco_width = int(input('Введите ширину шоколадки: '))
need_parts = int(input('Укажите, сколько долек нужно отломить: '))

if need_parts < choco_width * choco_length and (need_parts % choco_length == 0 or need_parts % choco_width == 0):
    print('YES')
else:
    print('NO')
