
import csv
import pandas as pd
from PyQt5 import uic, QtWidgets, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem


uf_tabela = pd.read_excel(f'.\dados\cidades.xls')
uf = uf_tabela["UF"]
cidade = uf_tabela["cidade"]

if __name__ == '__main__':
    App = QtWidgets.QApplication([])
    
    frm_cadColab = uic.loadUi(r'.\frms\frm_cadastroColab.ui')
    # botões da tela cadastro colaborador
    frm_cadColab.comboBox_funcao.addItems(["Motorista","Coferente","Aux. ADM"])
    frm_cadColab.comboBox_cidade.addItems(cidade)
    frm_cadColab.comboBox_uf.addItems(uf)
    frm_cadColab.show()
    App.exec()




