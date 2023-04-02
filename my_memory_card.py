from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import randint, shuffle 


class Question():
    ''' содержит вопрос, правильный ответ и три неправильных'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = [] 
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
questions_list.append(Question('Кто основатель Tesla', 'Илон Маск', 'Стив Джобс', 'Криштиану Роналдо', 'Борис Джонсон'))
questions_list.append(Question('Какая империя была самая крупная за всю историю', 'Британская', 'Французская', 'Российская', 'Монгольская'))
questions_list.append(Question('В каком году был распад СССР', '1991', '1987', '1945', '2002'))
questions_list.append(Question('В каком году началась Первая мировая война', '1914', '1945', '1991', '1867'))
questions_list.append(Question('В каком году началась вторая мировая война', '1939', '1984', '1914', '1991'))
questions_list.append(Question('Сколько было зубов у коня Чингисхана', '28', '14', '43', '24'))
questions_list.append(Question('Кто убил Гитлера', 'самоубийство', 'советские солдаты', 'американские солдаты', 'Сталин'))
questions_list.append(Question('Какую нация также называют ганцы', 'немцы', 'русские', 'американцы', 'французы'))
questions_list.append(Question('Какой самый крупно населенный город в мире', 'Токио', 'Нью-дели', 'Пекин', 'Вашингтон'))
questions_list.append(Question('Что означают звезды на флаге США', 'количество штатов', 'единство народа', 'силу неба', 'дом орла'))
questions_list.append(Question('Какая самая крупно населенная страна', 'Китай', 'Япония', 'Россия', 'США'))
questions_list.append(Question('Кем был Гитлер', 'диктатором', 'художником', 'певцом', 'евреем'))
questions_list.append(Question('Какая армия была у Японской империи', 'камикадзе', 'обычная армия', 'самурай', 'ниндзя'))
questions_list.append(Question('Как звали отца Чингисхана', 'Есугей', 'Тэмуджин', 'Хасар', 'Курулук'))
questions_list.append(Question('Как звали мать Чингисхана', 'Оэлун', 'Борте', 'Хулан', 'Есуй'))
questions_list.append(Question('Кто основал Apple', 'Стив Джобс', 'Илон Маск', 'Леонель Месси', 'Дональд Трамп'))
questions_list.append(Question('Столица Мадагаскара', 'Антананариву', 'Рабат', 'Анкара', 'Антарева'))
questions_list.append(Question('Какая религия у арабских стран', 'Ислам', 'Христианство', 'Буддизм', 'Атеизм'))
questions_list.append(Question('Кто убил Пушкина', 'Дантесс', 'Гитлер', 'Сталин', 'Чингисхан'))
questions_list.append(Question('Когда Казахстан получил независимость', '1991', '1945', '1872', '1238'))
questions_list.append(Question('Столица Канады', 'Оттава', 'Москва', 'Астана', 'Пекин'))
questions_list.append(Question('Столица Мексики', 'Мехико', 'Бразилиа', 'Улан-батор', 'Сан-Франциско'))
questions_list.append(Question('Кого ненавидел Гитлер', 'евреев', 'русских', 'англичан', 'немцев'))
questions_list.append(Question('Кто такой Пушкин', 'Писатель', 'диктатор', 'Нацист', 'военный'))
questions_list.append(Question('Кто был самым умным человеком на планете', 'Эйнштейн', 'Илон Маск', 'Гитлер', 'Пушкин'))
questions_list.append(Question('Кем был Шишкин', 'художник', 'раб', 'депутат', 'немец'))
questions_list.append(Question('Столица Японии', 'Токио', 'Москва', 'Алма-Ата', 'Киев'))
questions_list.append(Question('У кого самая сильная армия', 'США', 'Италия', 'Китай', 'Япония'))
questions_list.append(Question('Из чего состоит вселенная', 'Туманностей', 'Галактик', 'планет', 'звезд'))


app = QApplication([])


btn_OK = QPushButton('Ответить') # кнопка ответа
lb_Question = QLabel('Самый сложный вопрос в мире!') # текст вопроса


RadioGroupBox = QGroupBox("Варианты ответов") # группа на экране для переключателей с ответами


rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')


RadioGroup = QButtonGroup() # это для группировки переключателей, чтобы управлять их поведением
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке


RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов 


AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() # скроем панель с ответом, сначала должна быть видна панель вопросов


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)


layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(q: Question):
    ''' функция записывает значения вопроса и ответов в соответствующие виджеты, 
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers) # перемешали список из кнопок, теперь на первом месте списка какая-то непредсказуемая кнопка
    answers[0].setText(q.right_answer) # первый элемент списка заполним правильным ответом, остальные - неверными
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) # вопрос
    lb_Correct.setText(q.right_answer) # ответ 
    show_question() # показываем панель вопросов 


def show_correct(res):
    ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    lb_Result.setText(res)
    show_result()


def check_answer():
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        # правильный ответ!
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # неправильный ответ!
            show_correct('Неверно!')
            print('Рейтинг: ', (window.score/window.total*100), '%')
    


def next_question():
    ''' задает случайный вопрос из списка '''
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
    cur_question = randint(0, len(questions_list) - 1)  # нам не нужно старое значение, 
                                                        # поэтому можно использовать локальную переменную! 
            # случайно взяли вопрос в пределах списка
            # если внести около сотни слов, то редко будет повторяться
    q = questions_list[cur_question] # взяли вопрос
    ask(q) # спросили


def click_OK():
    ''' определяет, надо ли показывать другой вопрос либо проверить ответ на этот '''
    if btn_OK.text() == 'Ответить':
        check_answer() # проверка ответа
    else:
        next_question() # следующий вопрос


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')


btn_OK.clicked.connect(click_OK) # по нажатии на кнопку выбираем, что конкретно происходит


window.score = 0
window.total = 0
next_question()
window.resize(400, 300)
window.show()
app.exec()