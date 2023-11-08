from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('тестовый вопрос')

question = QLabel('Вопрос?')
btn_answer1 = QRadioButton('Ответ 1')
btn_answer2 = QRadioButton('Ответ 2')
btn_answer3 = QRadioButton('Ответ 3')
btn_answer4 = QRadioButton('Ответ 4')

layout_main = QVBoxLayout()
# layout_main.addWidget(question, alignment=Qt.AlignmentFlag.AlignCenter)
# layout_main.addWidget(btn_answer1, alignment=Qt.AlignmentFlag.AlignCenter)
# layout_main.addWidget(btn_answer2, alignment=Qt.AlignmentFlag.AlignCenter)
# layout_main.addWidget(btn_answer3, alignment=Qt.AlignmentFlag.AlignCenter)
# layout_main.addWidget(btn_answer4, alignment=Qt.AlignmentFlag.AlignCenter)

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH1.addWidget(question, alignment=Qt.AlignmentFlag.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment=Qt.AlignmentFlag.AlignCenter)
layoutH2.addWidget(btn_answer2, alignment=Qt.AlignmentFlag.AlignCenter)
layoutH3.addWidget(btn_answer3, alignment=Qt.AlignmentFlag.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment=Qt.AlignmentFlag.AlignCenter)

layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
main_win.setLayout(layout_main)


def show_win():
    victory_win = QMessageBox()
    victory_win.setText('Верно')
    victory_win.exec()


def show_lose():
    lose = QMessageBox()
    lose.setText('Не верно')
    lose.exec()


btn_answer1.clicked.connect(show_lose)
btn_answer2.clicked.connect(show_win)
btn_answer3.clicked.connect(show_lose)
btn_answer4.clicked.connect(show_lose)

main_win.show()
app.exec()
