import os
from pathlib import Path

# читаем файл
DIR = Path(__file__).resolve().parent  # путь до текущей папки
# print(DIR)
os.chdir(DIR)  # перейти в папку по пути

# 1
with open(DIR / 'my_file.txt', 'r') as file:
    summ = 0
    for string in file:
        summ += string.split().count('1')
    print(f'сумма единиц {summ}')

# 2
with open(DIR / 'my_file.txt', 'r') as file:
    for count, string in enumerate(file, start=1):
        if count == 14:
            print(string.split()[7])
            break

with open(DIR / 'my_file.txt', 'r') as file:
    lines = file.readlines()
    second_line = lines[13].split(' ')[7]
    print(second_line)
