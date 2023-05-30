#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QGroupBox, QWidget,QButtonGroup, QRadioButton,QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Одна из трёх реликвий Китая','Красный Заяц','Панда','Золотой Дракон','Копье Земли'))
questions_list.append(Question('Кто сильнейший враг Кунгфу-Панды','Кай','Тайлунг','Шень','Ки-Па'))
questions_list.append(Question('Что такое Рагнарёк','Битва между людьми и богами','Смерть богов','Пришествие Суртура','Пришествие Хеллы'))
questions_list.append(Question('Кто бог смерти Японии','Шинигами','Танатос','Анубис','Хелла'))
questions_list.append(Question('Сколько цветов Стича было показано в мультике Лило и Стич','4','3','5','2'))
questions_list.append(Question('Кто самый умный человек в мире','Мэрилин вос Савант','Никола Тесла','Илон Маск','Теренса Тао'))
questions_list.append(Question('Кто самый толстый человек в мире','Кэрол Йегер','Пол Джонатан','Хуан Педро Франко','Халид ибн Мухсен Шаари'))
questions_list.append(Question('Что делать, если тебя обвиняют в убийстве','Ждать, пока тебя оправдают','Самоубийство','Сознаться','Пойти и убить кого-то'))
questions_list.append(Question('Какой актёр Человека-Паука лучший','Все','Холланд','Гарфилд','Магуаер'))
questions_list.append(Question('Число ПИ','3.141592653589793238462','3.14159265729354961325','3.14159621265348969328','3.14'))

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memo Card')
btn_ok = QPushButton('Ответить')

lb_question=QLabel('Самый сложный вопрос в мире!')
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans_hor = QHBoxLayout()
layout_ans_ver1 = QVBoxLayout()
layout_ans_ver2 = QVBoxLayout()
layout_ans_ver1.addWidget(rbtn_1)
layout_ans_ver1.addWidget(rbtn_2)
layout_ans_ver2.addWidget(rbtn_3)
layout_ans_ver2.addWidget(rbtn_4)
layout_ans_hor.addLayout(layout_ans_ver1)
layout_ans_hor.addLayout(layout_ans_ver2)
RadioGroupBox.setLayout(layout_ans_hor)

AnsGroupBox = QGroupBox('Результат теста')
lb_result = QLabel('прав ты или нет?')
lb_correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct, alignment=Qt.AlignHCenter, stretch=1)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok,stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addStretch(1)
layout_card.addLayout(layout_line1)
layout_card.addStretch(1)

layout_card.addLayout(layout_line2, stretch=8)

layout_card.addStretch(1)
layout_card.addLayout(layout_line3)
layout_card.addStretch(1)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score +=1
        print('Статистика\n-Всего вопросов:',window.total,'\nПравильных ответов:',window.score,'\nРейтинг:', window.score/window.total*100,'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Статистика\n-Всего вопросов:',window.total,'\nПравильных ответов:',window.score,'\nРейтинг:',  window.score/window.total*100,'%')
def next_question():
    window.total+=1
    cur_question = randint(0,len(questions_list)-1)
    q = questions_list[cur_question]
    ask(q)

def click_OK():
    if btn_ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()


window.setLayout(layout_card)
window.score = 0
window.total = 0
btn_ok.clicked.connect(click_OK)
next_question()
window.resize(400,300)
window.show()
app.exec()