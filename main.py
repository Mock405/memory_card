from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QButtonGroup,
                             QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QRadioButton, QMessageBox, QGroupBox)
class Question():
    def __init__(self, question_text, right_answer, wrong1, wrong2, wrong3):
        self.q_text = question_text
        self.r_answer = right_answer
        self.w1_answer = wrong1
        self.w2_answer = wrong2
        self.w3_answer = wrong3
questions_list = []
q1 = Question('Самая быстрая машина в мире?', 'Koenigsegg Jesko Absolut', 'Lamborghini Huracan', 'Bugatti Chiron', 'Ferrari')
q2 = Question('Самая дорогая машина в мире?','Rolce Royse','Mercedes','Lamborgini','Ferrari')
q3 = Question('Самый мощный ноутбук в мире?','GPD WIN MAX2','Asus Rog','Asus Tuf','Hp')
questions_list.append(q1)
questions_list.append(q2)
questions_list.append(q3)
