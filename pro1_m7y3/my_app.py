from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from instr import *
from second_win import *


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()  # создаём и настраиваем графические элементы
        self.connects()  # устанавливает связи между элементами
        self.set_appear()  # устанавливает, как будет выглядеть окно
        self.show()  # старт

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.hello_txt = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(
            self.hello_txt, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(
            self.instruction, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(
            self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.layout)

    def connects(self):
        self.button.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw = TestWin()


app = QApplication([])
mw = MainWin()
app.exec()
