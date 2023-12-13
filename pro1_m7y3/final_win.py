# напиши здесь код третьего экрана приложения
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from instr import *


class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()  # устанавливает, как будет выглядеть окно
        self.initUI()  # создаём и настраиваем графические элементы
        self.show()  # старт

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.text_index = QLabel(txt_index)
        self.text_workheart = QLabel(txt_workheart)
        self.c_line = QVBoxLayout()
        self.c_line.addWidget(
            self.text_index, alignment=Qt.AlignmentFlag.AlignCenter)
        self.c_line.addWidget(self.text_workheart,
                              alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.c_line)
