# # Здесь должен быть твой код
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
df = pd.read_csv(DIR / 'titanic.csv')
print('выводим хэдер')
print(df.head())
print()

print('проверяем гипотезы')
print(df.groupby('Sex')['Survived'].mean())
print()

print(df.pivot_table(index='Survived', columns='Pclass', values='Age', aggfunc='mean'))
print()
print('удаляем лишние столбцы')
df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
print(df.head())
print()

print('очищаем датасет')
print(df['Embarked'].value_counts())
print()
df['Embarked'].fillna('S', inplace=True)

print('заполняем возраст')
print(df.groupby('Pclass')['Age'].median())
age_1 = df[df['Pclass'] == 1]['Age'].median()
age_2 = df[df['Pclass'] == 2]['Age'].median()
age_3 = df[df['Pclass'] == 3]['Age'].median()


def fill_age(row):
    if pd.isnull(row['Age']):
        if row['Pclass'] == 1:
            return age_1
        if row['Pclass'] == 2:
            return age_2
        return age_3
    return row['Age']


df['Age'] = df.apply(fill_age, axis=1)


def fill_sex(sex):
    if sex == 'male':
        return 1
    return 0


df['Sex'] = df['Sex'].apply(fill_sex)
print()

print('создаем фиктивные переменные в портах')
df[list(pd.get_dummies(df['Embarked']).columns)
   ] = pd.get_dummies(df['Embarked'])
df.drop('Embarked', axis=1, inplace=True)
print(df.head())
print(df.info())
print()

print('один ли пассажир?')


def is_alone(row):
    if row['SibSp'] + row['Parch'] == 0:
        return 1
    return 0


df['Alone'] = df.apply(is_alone, axis=1)
df.pivot_table(values='Age', columns='Alone',
               index='Survived', aggfunc='count')
print(df.head())
print(df.info())
print()

# делим набор на 2 части
x = df.drop('Survived', axis=1)  # данные о пассажирах
y = df['Survived']  # целевая переменная
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
# выполняем стандартизацию показателей в обоих наборах
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
# построение и обучение модели
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)
# предсказание судьбы пассажиров
y_pred = classifier.predict(X_test)
print('Процент правильно предсказанных исходов:',
      accuracy_score(y_test, y_pred) * 100)
