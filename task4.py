# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат 
# точек в этой четверти (x и y).


quarter = int(input('Введите номер четверти (от 1 до 4 включительно): '))

if quarter == 1:
    print ('Возможные значения х могут быть > 0, а y > 0')
if quarter == 2:
    print ('Возможные значения х могут быть < 0, а y > 0')
if quarter == 3:
    print ('Возможные значения х могут быть < 0, а y < 0')
if quarter == 4:
    print ('Возможные значения х могут быть > 0, а y < 0')
if quarter > 4:
    print('Такой четверти нет')