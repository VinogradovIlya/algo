from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
import json
import os
from pathlib import Path

# читаем файл
DIR = Path(__file__).resolve().parent  # путь до текущей папки
# print(DIR)
os.chdir(DIR)  # перейти в папку по пути


app = QApplication([])
main_win = QWidget()

notes = {
    'Добро пожаловать': {
        'text': 'Вводная инструкция',
        'tags': ['Умные заметки', 'Инструкция']
    }
}

with open(DIR/'notes_data.json', 'w', encoding='utf-8') as file:
    json.dump(notes, file)


def show_note() -> None:
    key = list_notes.selectedItems()[0].text()
    field_note.setText(notes[key]['text'])
    list_tags.clear()
    list_tags.addItems(notes[key]['tags'])


main_h_layout = QHBoxLayout()
add_left_layout = QVBoxLayout()
add_right_layout = QVBoxLayout()

main_h_layout.addLayout(add_left_layout)
main_h_layout.addLayout(add_right_layout)
main_win.setLayout(main_h_layout)

field_note = QTextEdit()
field_note.setText('Введите текст заметки')
add_left_layout.addWidget(field_note)

label_notes = QLabel('Список заметок')
list_notes = QListWidget()
add_h1_line = QHBoxLayout()
button_create_notes = QPushButton('Создать заметку')
button_remove_notes = QPushButton('Удалить заметку')
add_h1_line.addWidget(button_create_notes)
add_h1_line.addWidget(button_remove_notes)
button_save_notes = QPushButton('Сохранить заметку')

add_right_layout.addWidget(label_notes)
add_right_layout.addWidget(list_notes)
add_right_layout.addLayout(add_h1_line)
add_right_layout.addWidget(button_save_notes)

label_tags = QLabel('Список тегов')
list_tags = QListWidget()
add_h2_line = QHBoxLayout()
button_create_tags = QPushButton('Добавить к заметке')
button_remove_tags = QPushButton('Открепить от заметки')
tag_line = QLineEdit()
tag_line.setPlaceholderText('Введите тег')
add_h2_line.addWidget(button_create_tags)
add_h2_line.addWidget(button_remove_tags)
button_save_tags = QPushButton('Искать заметки по тегу')

add_right_layout.addWidget(label_tags)
add_right_layout.addWidget(list_tags)
add_right_layout.addWidget(tag_line)
add_right_layout.addLayout(add_h2_line)
add_right_layout.addWidget(button_save_tags)

list_notes.itemClicked.connect(show_note)

with open("notes_data.json", "r", encoding='utf-8') as file:
    notes = json.load(file)
list_notes.addItems(notes)


main_win.show()
app.exec()
