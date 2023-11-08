from PyQt6.QtCore import Qt
from random import randint
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Определитель победителя')

but = QPushButton('Сгенерировать')
text = QLabel('Нажми, чтобы узнать победителя')
winner = QLabel('?')
v_line = QVBoxLayout()

v_line.addWidget(text, alignment=Qt.AlignmentFlag.AlignCenter)
v_line.addWidget(winner, alignment=Qt.AlignmentFlag.AlignCenter)
v_line.addWidget(but, alignment=Qt.AlignmentFlag.AlignCenter)
main_win.setLayout(v_line)


def show_winner():
    number = randint(0, 99)
    winner.setText(str(number))
    text.setText('Победитель:')


but.clicked.connect(show_winner)

main_win.show()
app.exec()
