

import pandas as pd
import sqlite3
from PyQt5 import uic, QtWidgets, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem

banco = sqlite3.connect('banco_cadastro.db') 
cursor = banco.cursor()

tabela = pd.read_excel(f'.\dados\cidades.xls')
cidade = tabela.loc[tabela["UF"]=="RS"]
uf = tabela.loc[tabela["UF"]=="RS"]
tabela_funcao = pd.read_excel(r'.\dados\funcoes.xlsx')



def cadastra_funcao():
    
    tabela.to_excel(r'.\dados\funcoes.xlsx', index = False)
def chamacadfuncao():
    frm_funcao.show()
    frm_funcao.edt_funcao.setText("")
    
def chamacadColab():
    frm_cadColab.show()
def fechacolab():
    frm_cadColab.close()
if __name__ == '__main__':
    App = QtWidgets.QApplication([])
    frm_inicial = uic.loadUi(r'.\frms\frm_principal.ui')
    frm_cadColab = uic.loadUi(r'.\frms\frm_cadastroColab.ui')
    frm_funcao = uic.loadUi(r'.\frms\frm_funcao.ui')
    frm_inicial.actionCadastrar.triggered.connect(chamacadColab)
    frm_inicial.actionCadastrar_Fun.triggered.connect(chamacadfuncao)
    frm_inicial.label.setPixmap(QtGui.QPixmap(r'.\logo\do-utilizador.png'))
    frm_inicial.label.resize(520,550)

    # botões da tela cadastro funcao
    frm_funcao.btn_salvar.clicked.connect(cadastra_funcao)

    # botões da tela cadastro colaborador
    frm_cadColab.btn_fechar.clicked.connect(fechacolab)
    frm_cadColab.comboBox_uf.addItems(uf["UF"])
    frm_cadColab.comboBox_cidade.addItems(cidade["cidade"])
    frm_cadColab.comboBox_funcao.addItems(tabela_funcao["descricao"])
    


    frm_cadColab.show()
    App.exec()




