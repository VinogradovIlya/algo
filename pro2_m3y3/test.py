
import pandas as pd
import os
from pathlib import Path

# читаем файл
DIR = Path(__file__).resolve().parent  # путь до текущей папки
# print(DIR)
os.chdir(DIR)  # перейти в папку по пути


df = pd.read_csv(DIR / 'GooglePlayStore_wild.csv')


# Очистка данных из первого задания
df['Rating'].fillna(-1, inplace=True)


def set_size(size):
    if size[-1] == 'M':
        return float(size[:-1])
    elif size[-1] == 'k':
        return float(size[:-1]) / 1024
    return -1


df['Size'] = df['Size'].apply(set_size)


def set_installs(installs):
    if installs == '0':
        return 0
    return int(installs[:-1].replace(',', ''))


df['Installs'] = df['Installs'].apply(set_installs)


df['Type'].fillna('Free', inplace=True)


# Замени тип данных на дробное число (float) для цен приложений ('Price')
def make_price(price):
    if price[0] == '$':
        return float(price[1:])
    return 0


df['Price'] = df['Price'].apply(make_price)


# Вычисли, сколько долларов разработчики заработали на каждом платном приложении
df['Profit'] = df[df['Installs'] != 0]['Installs'] * df['Price']
print(df['Profit'])

