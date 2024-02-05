import sqlite3
db_name = 'quiz.sqlite'
conn = None
curor = None


def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()


def close():
    cursor.close()
    conn.close()


def do(query):
    cursor.execute(query)
    conn.commit()


def clear_db():
    ''' удаляет все таблицы '''
    open()
    query = '''DROP TABLE IF EXISTS quiz_content'''
    do(query)
    query = '''DROP TABLE IF EXISTS question'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz'''
    do(query)
    close()


def create():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')
    do('''CREATE TABLE IF NOT EXISTS quiz_content(
    id INTEGER PRIMARY KEY,
    quiz_id INTEGER,
    question_id INTEGER,
    FOREIGN KEY (quiz_id) REFERENCES quiz (id)''')

    do(''' CREATE TABLE IF NOT EXISTS question(
    id INTEGER PRIMARY KEY,
    question_id INTEGER,
    answer_id INTEGER,
    wrong1_id INTEGER,
    wrong2_id INTEGER,
    wrong3_id INTRGER,
    FOREIGN KEY (id) REFERENCES quiz_content (question_id)''')

    do(''' CREATE TABLE IF NOT 
    id INTEGER PRIMARY KEY,EXISTS quiz(
    name VARCHAR)''')
    close()


def answer1():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')
    query = "INSERT INTO quiz_content (quiz_id, question_id)VALUES (?,?)"
    answer = input('Добавить связь (y / n)?')
    while answer != 'n':
        quiz_id = int(input('id викторины:'))
        question_id = int(input('id вопроса:'))
        cursor.execute(query, [quiz_id, question_id])
        conn.commit()
        answer = input('Добавить связь (y / n)?')
    close()


def quizes1():
    quizes = [
        ('Своя игра', ),
        ('Кто хочет стать миллионером')
        ('Самый умный', )]
    open()
    cursor.executemany(""" INSERT INTO quiz(name) VALUES (?) """, quizes)
    conn.commit()
    close()


def question1():
    questions = [
        ('Сколько месяцев в году имеют 28 дней', 'Все', "Один", "Ни одного", "Два")
        ('Каким станет зеленый утес, если упадет в Красное море?',
         'Мокрым', 'Красным', 'Не изменится', 'Фиолетовым'),
        ('Какой рукой лучше размешивать чай?',
         'Ложкой', 'Правой', 'Левой', 'Любой'),
        ('Что не имеет длины, глубины, ширины, высоты, а можно измерить?',
         'Время', 'Глупость', 'Море', 'Воздух'),
        ('Когда сетью можно вытянуть воду?', 'Когда вода замерзла',
         'Когда нет рыбы', 'Когда уплыла золотая рыбка', 'Когда сеть порвалась'),
        ('Что больше слона и ничего не весит?', 'Тень слона', 'Воздушный шар', 'Парашют', 'Облако')]
    open()
    cursor.executemany(
        """ INSERT INTO question(question, answer, wrong1, wrong2, wrong3) VALUES(?,?,?,?,?)""", questions)
    conn.commit()
    close()


def get_question_after(question_id=0, quiz_id=1):
    open()
    zapr = """ SELECT quiz_content.id, question.question, question.answer, question.wrong1,
    question.wrong2, question.wrong3
    FROM quiz_content, question
    WHERE quiz_content.question_id == question.id 
    AND quiz_content.id > ?
    AND quiz_content.quiz_id == ?
    ORDER BY quiz_content.id """
    cursor.executemany(zapr, [question_id, quiz_id])
    per = cursor.fetchone()
    close()
    return per


def show(table):
    query = 'SELECT * FROM ' + table
    open()
    cursor.execute(query)
    print(cursor.fetchall())
    close()


def show_tables():
    show('question')
    show('quiz')
    show('quiz_content')


def main():
    clear_db()
    create()
    quizes1()
    question1()
    answer1()
    show_tables()
    print(get_question_after(3, 1))


if __name__ == "__main__":
    main()