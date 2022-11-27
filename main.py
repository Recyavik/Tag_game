import random
import os
import time
import pyfiglet
from progress.bar import IncrementalBar

print(pyfiglet.figlet_format('MERRY CRISTMAS'))
input('Нажмите Enter для начала игры ')
mylist = [10, 22, 35, 44, 60, 69, 78, 100]
bar = IncrementalBar('Загрузк: ', max=len(mylist))
for item in mylist:

    bar.next()
    time.sleep(random.uniform(0, 0.3))
bar.finish()

if os.name == 'nt':
    os.system('cls')
else:
    print('не смог очистить консоль')
number_list = [i for i in range(1, 16)]
number_list.append('_')

result_list = list(zip(*[iter(number_list)] * 4))
for i in range(len(result_list)):
    result_list[i] = list(result_list[i])
print(result_list)

random.shuffle(number_list)
area = list(zip(*[iter(number_list)] * 4))
for i in range(len(area)):
    area[i] = list(area[i])
print(area)
col_width = max(len(str(num)) for row in area for num in row) + 2
while result_list != area:
    if os.name == 'nt':
        os.system('cls')
    else:
        print('не смог очистить консоль')

    for row in area:
        print(''.join(str(num).ljust(col_width) for num in row))
    row1 = int(input('Введите строку откуда')) - 1
    collumn1 = int(input('Введите столбец откуда')) - 1
    row2 = int(input('Введите строку куда')) - 1
    collumn2 = int(input('Введите столбец куда')) - 1
    if area[row2][collumn2] == '_':
        area[row2][collumn2], area[row1][collumn1] = area[row1][collumn1], area[row2][collumn2]
    else:
        print('Ячейка занята ')
        continue
print('Поздравляю! вы победили!')
