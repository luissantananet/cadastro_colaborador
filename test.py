import sqlite3
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItem, QStandardItemModel

# Conecte-se ao banco de dados e execute a consulta
banco = sqlite3.connect(r'.\dados\banco_cadastro.db') 
cursor = banco.cursor()
cursor.execute("select * from cadastro_colaborador")
banco.commit()
dados = cursor.fetchall()

# Crie um modelo de item padrão para a tabela
modelo = QStandardItemModel(len(dados),1)
modelo.setHorizontalHeaderLabels(['ID','Nome Completo'])

# Adicione os dados ao modelo
for i in range(len(dados)):
    for j in range(2):
        item = QStandardItem(str(dados[i][j]))
        modelo.setItem(i, j, item)

# Crie um filtro e aplique-o ao modelo
filtro = QSortFilterProxyModel()
filtro.setSourceModel(modelo)
filtro.setFilterKeyColumn(1)
filtro.setFilterCaseSensitivity(Qt.CaseInsensitive)

if __name__ == '__main__':
    App = QtWidgets.QApplication([])
    frm_inicial = uic.loadUi(r'.\frms\frm_pesquisarColabRegistro2.ui')
    frm_inicial.tableView.setModel(filtro)
    frm_inicial.tableView.horizontalHeader().setStyleSheet("font-size: 15px;color: rgb(50, 50, 255);")
    frm_inicial.edt_pesquisar.textChanged.connect(filtro.setFilterRegExp)
    frm_inicial.show()
    App.exec()
