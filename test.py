

from msilib.schema import tables
import pandas as pd
import sqlite3
from PyQt5 import uic, QtWidgets, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem

banco = sqlite3.connect('banco_cadastro.db') 
cursor = banco.cursor()
cursor.execute("select * from tabela")
dados = cursor.fetchall()
banco.commit()
tables = len(dados)

print(tables)

if tables == 0:
    print("ok")
else:
    print("erro")


