# создай приложение для запоминания информации
from random import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


def ask(q1):
    shuffle(box)
    box[0].setText(q1.right_answer)
    box[1].setText(q1.wrong1)
    box[2].setText(q1.wrong2)
    box[3].setText(q1.wrong3)
    lab.setText(q1.question)
    text.setText(q1.right_answer)
    show_question()


def show_result():
    radio_group_box.hide()
    answer_group.show()
    button.setText('Следующий вопрос')


def next_question():
    main_win.num += 1
    if main_win.num >= len(questions_list):
        main_win.num = 0
    ask(questions_list[main_win.num])


def show_question():
    answer_group.hide()
    radio_group_box.show()
    button.setText('Ответить')
    radio_group.setExclusive(False)
    button_1.setChecked(False)
    button_2.setChecked(False)
    button_3.setChecked(False)
    button_4.setChecked(False)
    radio_group.setExclusive(True)


def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    elif button.text() == 'Следующий вопрос':
        next_question()


def check_answer():
    if box[0].isChecked():
        text_win.setText('Правильно!')
    else:
        text_win.setText('Неправильно!')
    show_result()


app = QApplication([])
main_win = QWidget()
main_win.resize(700, 500)
main_win.setWindowTitle('Memory Card')
main_win.move(200, 600)
main_win.num = -1

x_line = QHBoxLayout()
z_line = QHBoxLayout()
p_line = QHBoxLayout()
y_line = QVBoxLayout()
t_line = QVBoxLayout()

radio_group_box = QGroupBox('Варианты ответов')
button = QPushButton('Ответить')
button.clicked.connect(click_ok)
button_1 = QRadioButton('Энцы')
button_2 = QRadioButton('Смурфы')
button_3 = QRadioButton('Чулымцы')
button_4 = QRadioButton('Алеуты')
box = [button_1, button_2, button_3, button_4]
lab = QLabel('Какой национальности не существует?')
radio_group = QButtonGroup()
radio_group.addButton(button_1)
radio_group.addButton(button_2)
radio_group.addButton(button_3)
radio_group.addButton(button_4)
# radio_group_box.hide()

main_win.setLayout(y_line)
p_line.addStretch(1)
p_line.addWidget(button, stretch=2)
p_line.addStretch(1)

x_line.addWidget(button_1, alignment=Qt.AlignmentFlag.AlignCenter)
x_line.addWidget(button_3, alignment=Qt.AlignmentFlag.AlignCenter)
z_line.addWidget(button_2, alignment=Qt.AlignmentFlag.AlignCenter)
z_line.addWidget(button_4, alignment=Qt.AlignmentFlag.AlignCenter)
t_line.addLayout(x_line)
t_line.addLayout(z_line)
radio_group_box.setLayout(t_line)

############
answer_group = QGroupBox('Результат теста')
num_1 = QHBoxLayout()
num_2 = QVBoxLayout()
num_3 = QHBoxLayout()
answer_group.hide()

text_win = QLabel('Правильно/Неправильно')
text = QLabel('Энцы')

answer_group.setLayout(num_2)
num_2.addWidget(text_win, alignment=Qt.AlignmentFlag.AlignLeft |
                Qt.AlignmentFlag.AlignTop)
num_2.addWidget(text, alignment=Qt.AlignmentFlag.AlignCenter)

y_line.addWidget(lab, alignment=Qt.AlignmentFlag.AlignCenter)
y_line.addWidget(radio_group_box)
y_line.addWidget(answer_group)
y_line.addLayout(p_line)
y_line.setSpacing(10)
y_line.addLayout(p_line)
y_line.setSpacing(10)

q1 = Question('Государственный язык Бразилии', 'Португальский',
              'Испанский', 'Итальянский', 'Бразильский')
questions_list = []
questions_list.append(Question('Государственный язык Бразилии',
                      'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(Question(
    'Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(
    Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))

main_win.show()
app.exec()
