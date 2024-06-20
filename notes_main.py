#начни тут создавать приложение с умными заметками
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout


import json




app = QApplication([])
notes = {'Моя первая заметка':
            {'текст':'всем здрастьте',
                'теги':['приветствие','первая']
            }
}   
'''
with open('f.json','w',encoding='utf-8') as file:
    json.dump(notes,file,sort_keys=True)
    '''
win = QWidget()
win.setWindowTitle('Умные заметки')
win.resize(900,600)
f_text = QTextEdit()

list_notes_Label = QLabel('Список заметок')
list_notes = QListWidget()
but_notes_add = QPushButton('Создать заметку')
but_notes_del = QPushButton('Удалить заметку')
but_notes_save = QPushButton('Сохранить заметку')

list_tegs_Label = QLabel('Список тегов')
list_tags = QListWidget()
f_tag = QLineEdit('')
f_tag.setPlaceholderText('Введите тег...')
but_tags_add = QPushButton('Добавить к заметке')
but_tags_del = QPushButton('Открепить от заметки')
but_tags_search = QPushButton('Искать заметки по тегу')

col1 = QVBoxLayout()
col1.addWidget(f_text)

col2 = QVBoxLayout()
col2.addWidget(list_notes_Label)
col2.addWidget(list_notes)

rof1 = QHBoxLayout()
rof1.addWidget(but_notes_add)
rof1.addWidget(but_notes_del)
rof2 = QHBoxLayout()
rof2.addWidget(but_notes_save)

col2.addLayout(rof1)
col2.addLayout(rof2)


col2.addWidget(list_tegs_Label)
col2.addWidget(list_tags)
col2.addWidget(f_tag)


kof1 = QHBoxLayout()
kof1.addWidget(but_tags_add)
kof1.addWidget(but_tags_del)
kof2 = QHBoxLayout()
kof2.addWidget(but_tags_search)
col2.addLayout(kof1)
col2.addLayout(kof2)

main_l = QHBoxLayout()
main_l.addLayout(col1)
main_l.addLayout(col2)

win.setLayout(main_l)
def add_note():
    note_name,result = QInputDialog.getText(win,'Добавить заметку','Название заметки')
    if result and note_name != '':
        notes[note_name] = {'текст':'','теги':[]}
        list_notes.addItem(note_name)
        list_tags.clear()

def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        f_text.clear()
        list_notes.addItems(notes)
        with open('f.json','w',encoding='utf-8') as file:
            json.dump(notes,file,sort_keys=True)
    else:
        print('Заметка для удаления не выбрана')
def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]['текст'] = f_text.toPlainText()
        with open('f.json','w',encoding='utf-8') as file:
            json.dump(notes,file,sort_keys=True)
    else:
        print('Заметка для сохранения  не выбрана')
def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = f_tag.text()
        if not tag in notes[key]['теги']:
            notes[key]['теги'].append(tag)
            list_tags.addItem(tag)
            f_tag.clear()
        with open('f.json','w',encoding='utf-8') as file:
            json.dump(notes,file,sort_keys=True)
    else:
        print('заметка для добавления тега не выбрана')
def del_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]['теги'].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key]['теги'])
        with open('f.json','w',encoding='utf-8') as file:
            json.dump(notes,file,sort_keys=True)
    else:
        print('тег для удаления не выбран')
def search_tag():
    tag = f_tag.text()
    if but_tags_search.text() == 'Искать заметки по тегу':
        notes_filtr = {}
        for note in notes:
            if tag in notes[note]['теги']:
                notes_filtr[note] = notes[note]
        but_tags_search.setText('Сбросить поиск')
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_filtr)
    elif but_tags_search.text() == 'Cбросить поиск':
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems()
        but_tags_search.setText('Искать заметки по тегу')




    
                    
        



def show_note():
    name  = list_notes.selectedItems()[0].text()
    f_text.setText(notes[name]['текст'])
    list_tags.clear()
    list_tags.addItems(notes[name]['теги'])

list_notes.itemClicked.connect(show_note)
but_notes_add.clicked.connect(add_note)
but_notes_del.clicked.connect(del_note)
but_notes_save.clicked.connect(save_note)
but_tags_add.clicked.connect(add_tag)
but_tags_del.clicked.connect(del_tag)
but_tags_search.clicked.connect(search_tag)






win.show()
with open('f.json','r',encoding='utf-8') as file:
    notes = json.load(file)
list_notes.addItems(notes)
app.exec_()
