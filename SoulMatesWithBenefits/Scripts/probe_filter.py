# -*- coding: utf-8 -*-

import pandas as pd
from sys import argv
from sys import exit


path = '/home/nnmd/Документы/'


try: 
    arg = str(argv[1])
except:
    arg = input(f'Введите имя файла: (папка по умолчанию: {path})\n')

try:
    df = pd.read_csv(path + arg, names=['Time', 'Strength', 'MAC-address', 'ESSID'], sep=' ')
except FileNotFoundError:
    print('Неверное имя файла. Првоерьте путь и имя файла и попробуйте еще раз.')
    exit()

print(df)

filtered = df[['MAC-address', 'ESSID']]
filtered = filtered.drop_duplicates().sort_values(by='MAC-address')
print(filtered)
filtered.to_csv(path+'filtered_probes.txt')

to_count = filtered['MAC-address']
to_count = to_count.drop_duplicates()
count = to_count.count()
print(f'Всего уникальных устройств обнаружено: {count}')
