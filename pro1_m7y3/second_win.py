# напиши здесь код для второго экрана приложения
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from instr import *
from final_win import *


class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()  # устанавливает, как будет выглядеть окно
        self.initUI()  # создаём и настраиваем графические элементы
        self.connects()  # устанавливает связи между элементами
        self.show()  # старт

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.move(win_x, win_y)
        self.resize(win_width, win_height)

    def initUI(self):
        # кнопки
        self.btn_next = QPushButton(txt_sendresults)
        self.btn_test1 = QPushButton(txt_starttest1)
        self.btn_test2 = QPushButton(txt_starttest2)
        self.btn_test3 = QPushButton(txt_starttest3)

        # надписи
        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)
        self.text_timer = QLabel(txt_timer)

        # поля ввода
        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)

        # лэйауты
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.r_line.addWidget(
            self.text_timer, alignment=Qt.AlignmentFlag.AlignCenter)

        self.l_line.addWidget(
            self.text_name, alignment=Qt.AlignmentFlag.AlignLeft)
        self.l_line.addWidget(
            self.line_name, alignment=Qt.AlignmentFlag.AlignLeft)
        self.l_line.addWidget(
            self.text_age, alignment=Qt.AlignmentFlag.AlignLeft)
        self.l_line.addWidget(
            self.line_age, alignment=Qt.AlignmentFlag.AlignLeft)
        self.l_line.addWidget(
            self.text_test1, alignment=Qt.AlignmentFlag.AlignLeft)
        self.l_line.addWidget(
            self.btn_test1, alignment=Qt.AlignmentFlag.AlignLeft)
        self.l_line.addWidget(
            self.line_test1, alignment=Qt.AlignmentFlag.AlignLeft)
        self.l_line.addWidget(
            self.text_test2, alignment=Qt.AlignmentFlag.AlignLeft)
        self.l_line.addWidget(
            self.btn_test2, alignment=Qt.AlignmentFlag.AlignLeft)
        self.l_line.addWidget(
            self.line_test2, alignment=Qt.AlignmentFlag.AlignLeft)
        self.l_line.addWidget(
            self.text_test3, alignment=Qt.AlignmentFlag.AlignLeft)
        self.l_line.addWidget(
            self.btn_test3, alignment=Qt.AlignmentFlag.AlignLeft)
        self.l_line.addWidget(
            self.line_test3, alignment=Qt.AlignmentFlag.AlignLeft)
        self.l_line.addWidget(
            self.btn_next, alignment=Qt.AlignmentFlag.AlignCenter)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.btn_test1.clicked.connect(self.timer_test)

    def next_click(self):
        self.hide()
        self.fw = FinalWin()

    def timer_test(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont("Times New Roman", 36))
        # self.text_timer.font().setBold(True)
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
