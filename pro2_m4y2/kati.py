from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import os
from pathlib import Path
# читаем файл
DIR = Path(__file__).resolve().parent  # путь до текущей папки
# print(DIR)
os.chdir(DIR)  # перейти в папку по пути
df = pd.read_csv(DIR / 'train.csv')

# print(df.groupby(by = 'result')['education_form'].value_counts())
# print(df[df['result']==0]['bdate'].value_counts().tail(50))
"""
id, has_photo, has_mobile, followers_count, graduation, people_main, career_start,
career_end, relation, education_status, occupation_type, occupation_name
"""
string = 'id, has_photo, has_mobile, followers_count, graduation, people_main, career_start, career_end, relation, education_status, occupation_type, occupation_name'.split(
    ', ')
# Удаляем лишние столбцы
df.drop(string, axis=1, inplace=True)
# Преобразовываем sex в 0  и  1


def set_sex(Sex):
    if Sex == 1:
        return 0
    return 1


df['sex'] = df['sex'].apply(set_sex)
# Преобразование education_form
# print(df.groupby(by = 'result')['education_form'].value_counts())
df[list(pd.get_dummies(df['education_form']).columns)
   ] = pd.get_dummies(df['education_form'])
df.drop('education_form', axis=1, inplace=True)
# Люди  указывающие 1,6,5 - 0 , 6,1,5,7 - 1   ---> 1, остальное -----> 0


def set_life_main(Life_main):
    if Life_main in [6, 1, 5, 7, 'False', 0]:
        return 1
    return 0


df['life_main'] = df['life_main'].apply(set_life_main)


def set_city(City):
    if City in ['Moscow', 'Saint Petersburg', 'Kyiv', 'Yekaterinburg', 'Minsk', 'Rostov-on-Don', 'Nizhny Novgorod', 'Odessa', 'Kazan']:
        return 1
    return 0


df['city'] = df['city'].apply(set_city)


def split_langs(Langs):
    return Langs.split(';')


df["langs"] = df["langs"].apply(split_langs)


def set_langs(Langs):
    if "English" in Langs and len(Langs) >= 2:
        return 1
    return 0


df['langs'] = df['langs'].apply(set_langs)


def set_bdate(Bdate):
    if pd.isnull(Bdate):
        return 0
    else:
        if '.' in Bdate[-4:]:
            return 0
        else:
            return int(Bdate[-4:])


df['bdate'] = df['bdate'].apply(set_bdate)
# print(df['bdate'].value_counts().head(50))


def set_last_seen(Last_seen):
    last = Last_seen.split('-')
    last = last[0:2]
    return last


df['last_seen'] = df['last_seen'].apply(set_last_seen)


def set_year(Year):
    return int(Year[0])


df['year'] = df['last_seen'].apply(set_year)


def set_month(Month):
    if Month[1][0] == '0':
        return int(Month[1][1])
    return int(Month[1])


df['month'] = df['last_seen'].apply(set_month)
df.drop('last_seen', axis=1, inplace=True)
# print(df.groupby(by = 'result')['last_seen'].head(50))
df.info()
# Шаг 2. Создание модели

X = df.drop('result', axis=1)
y = df['result']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.40)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
classifier = KNeighborsClassifier(n_neighbors=9)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print('Процент правильно предсказанных исходов:',
      accuracy_score(y_test, y_pred) * 100)
print('Confusion matrix:')
print(confusion_matrix(y_test, y_pred))
