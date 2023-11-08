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

# print(df.groupby(by = 'result')['has_mobile'].value_counts())
# bdate?
# Удаляем лишние столбцы id, has_photo, followers_count, relation, life_main, people_main, last_seen, occupation_name
drop_list = 'id, has_photo, followers_count, relation, life_main, people_main, last_seen, occupation_name'.split(
    ', ')
df.drop(drop_list, axis=1, inplace=True)
# sex 2 и 1  замнить 0  и  1


def set_sex(Sex):
    if Sex == 1:
        return 0
    return 1


df['sex'] = df['sex'].apply(set_sex)
# Преобразование has_mobile. В столбце тип данных float преобразуем это для int
df['has_mobile'] = df['has_mobile'].apply(int)
# Преобразование education_form заменим пустоты на самое частовстречаемое значение
df['education_form'].fillna('Full-time', inplace=True)
# создаем  фиктивную переменную
df[list(pd.get_dummies(df['education_form']).columns)
   ] = pd.get_dummies(df['education_form'])
# удаляем исходный столбец
df.drop('education_form', axis=1, inplace=True)
# Преобразуем education_status, создаем  фиктивную переменную
df[list(pd.get_dummies(df['education_status']).columns)
   ] = pd.get_dummies(df['education_status'])
# удаляем исходный столбец
df.drop('education_status', axis=1, inplace=True)
# Преобразуем occupation_type, заменим пустоты на самое частовстречаемое значение
df['occupation_type'].fillna('university', inplace=True)
# создаем  фиктивную переменную
df[list(pd.get_dummies(df['occupation_type']).columns)
   ] = pd.get_dummies(df['occupation_type'])
# удаляем исходный столбец
df.drop('occupation_type', axis=1, inplace=True)
# Преобразуем langs
langs_dict = dict()


def set_langs(Langs):
    Langs = Langs.split(';')
    for i in Langs:
        if i in langs_dict:
            langs_dict[i] += 1
        else:
            langs_dict[i] = 1
    return Langs


df['langs'] = df['langs'].apply(set_langs)
max_langs = 0
name_langs = ''
for lang in langs_dict:
    if max_langs < langs_dict[lang]:
        max_langs = langs_dict[lang]
        name_langs = lang
print(langs_dict)
print(name_langs)


def set_count_langs(Langs):
    return len(Langs)


df['langs_count'] = df['langs'].apply(set_count_langs)
print(df.groupby(by='result')['langs_count'].value_counts())


def set_langs1(Langs):
    langs_max = {'Русский', 'English', 'Українська',
                 'Deutsch', 'Français', 'Español', 'Italiano'}
    Langs = set(Langs)
    total = len(langs_max.intersection(Langs))
    if total == 0:
        return 0
    return 1


df['langs_log'] = df['langs'].apply(set_langs1)
print(df.groupby(by='result')['langs_log'].value_counts())
# исследовав столбец с языками получили,  что  язык слабо влияет  на то, будет  ли человек покупать курсы, поэтому удалить.
df.drop('langs', axis=1, inplace=True)
# Преобразуем city
city_list = ['', '']


def set_city(City):
    if City in city_list:
        return 1
    return 0


# исследовав столбец с  городами, выяснили,  что  он не влияет  на покупку курса
df.drop('city', axis=1, inplace=True)
df.drop('graduation', axis=1, inplace=True)
# Преобразуем bdate


def set_bdate(Bdate):
    Bdate = str(Bdate).split('.')
    if len(Bdate) == 3:
        return int(Bdate[2])
    return 0


df['bdate'] = df['bdate'].apply(set_bdate)
# print(df.groupby(by = 'result')['bdate'].value_counts())
# Преобразуем career_start


def set_career_start(start):
    if start == 'False':
        return 0
    return int(start)


df['career_start'] = df['career_start'].apply(set_career_start)
# print(df.groupby(by = 'result')['career_start'].value_counts())
df.drop('career_start', axis=1, inplace=True)
# Преобразуем career_end


def set_career_end(end):
    if end == 'False':
        return 0
    return int(end)


df['career_end'] = df['career_end'].apply(set_career_end)
# print(df.groupby(by = 'result')['career_end'].value_counts())
df.drop('career_end', axis=1, inplace=True)
df.info()
# Шаг 2. Создание модели
X = df.drop('result', axis=1)
y = df['result']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.40)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print('Процент правильно предсказанных исходов:',
      accuracy_score(y_test, y_pred) * 100)
print('Confusion matrix:')
print(confusion_matrix(y_test, y_pred))
