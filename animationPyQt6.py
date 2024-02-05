from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import QTimer


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Button")
        self.button.setGeometry(100, 100, 100, 50)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.move_button)

        self.move_up = True
        self.distance = 10

    def move_button(self):
        x = self.button.x()
        y = self.button.y()

        if self.move_up:
            y -= self.distance
            if y <= 0:
                self.move_up = False
        else:
            y += self.distance
            if y >= self.height() - self.button.height():
                self.move_up = True

        self.button.move(x, y)

    def start_animation(self):
        self.timer.start(50)


if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    window.setWindowTitle("Button Animation")
    window.setGeometry(100, 100, 300, 200)
    window.show()

    window.start_animation()
    app.exec()
