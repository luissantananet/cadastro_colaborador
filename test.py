

import pandas as pd
import sqlite3
from PyQt5 import uic, QtWidgets, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem

banco = sqlite3.connect('banco_cadastro.db') 
cursor = banco.cursor()
cursor.execute("SELECT cpf FROM cadastro_colaborador")
cpf_ = cursor.fetchall()
banco.commit()

cpf = '07261662437'
test = (cpf_[0])
if cpf == cpf_:
    print("cpf correto" )
else:
    print('cpf incorreto')
print(type(test))
print(type)

