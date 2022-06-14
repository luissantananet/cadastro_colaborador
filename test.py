import sqlite3
from PyQt5 import uic, QtWidgets, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItem, QStandardItemModel

banco = sqlite3.connect('banco_cadastro.db') 
cursor = banco.cursor()
cursor.execute("select * from cadastro_colaborador")
dados = cursor.fetchall()
banco.commit()
tabelas = dados

carros = ('Gol', 'Celta', 'Corsa', 'Uno', 'Fox', 'Cruze', 'Brasilia', 'Saveiro', 'Fusca', 'Hilux', 'Onix')




"""for i in range(0, len(tabelas)):
        for j in range(0, 10):
           modelo.setItem(i,0,elemento)"""
    
for i in range(0, len(tabelas)):
        for j in range(0, 10):
           tabela =(str(tabelas[i][j]))
print(type(tabela))
print(tabela)    

modelo = QStandardItemModel(len(tabelas),1)
modelo.setHorizontalHeaderLabels(['Nome'])
#elemento = QStandardItem(tabelas)

filtro = QSortFilterProxyModel()
filtro.setSourceModel(modelo)
filtro.setFilterKeyColumn(0)
filtro.setFilterCaseSensitivity(Qt.CaseInsensitive)

if __name__ == '__main__':
    App = QtWidgets.QApplication([])
    frm_inicial = uic.loadUi(r'.\frms\frm_pesquisarColabRegistro.ui')
    frm_inicial.tableView.setModel(filtro)
    frm_inicial.tableView.horizontalHeader().setStyleSheet("font-size: 15px;color: rgb(50, 50, 255);")
    frm_inicial.edt_pesquisar.textChanged.connect(filtro.setFilterRegExp)
    frm_inicial.show()
    App.exec()

