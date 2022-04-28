

import pandas as pd
import sqlite3
from PyQt5 import uic, QtWidgets, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem

banco = sqlite3.connect('banco_cadastro.db') 
cursor = banco.cursor()

uf_tabela = pd.read_excel(f'.\dados\cidades.xls')
cidade = uf_tabela["cidade"]
uf = uf_tabela["UF"]
funcaos_ = []
cursor.execute("SELECT descricao FROM funcao;")
dados_lidos = cursor.fetchall()

funcaos_ = dados_lidos
print(type(funcaos_))
print(funcaos_)
print(funcaos_[3])


def cadastra_funcao():
    descs = frm_funcao.edt_funcao.text()
    try:
        # cria o bando se ele nao exixtir 
        cursor.execute("CREATE TABLE IF NOT EXISTS funcao ( id INTEGER PRIMARY KEY AUTOINCREMENT, descricao varchar(100) NOT NULL);")
        cursor.execute("INSERT INTO funcao VALUES (NULL,'"+descs+"');")
        QMessageBox.information(frm_cadColab, "Aviso", "Função cadastrado com sucesso")
    except sqlite3.Error as erro:
        print("ERRO","Erro ao inserir os dados: ",erro)
    banco.commit()
def chamacadfuncao():
    frm_funcao.show()
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
    
    frm_cadColab.comboBox_uf. clearEditText()
    frm_cadColab.comboBox_uf.addItems(uf_tabela["UF"])
    uf = frm_cadColab.comboBox_uf.currentText()
    frm_cadColab.btn_fechar.clicked.connect(fechacolab)
    cid = uf_tabela["UF"] == str(uf)
   

    frm_cadColab.comboBox_cidade.addItems(cidade)
    
    
    
    frm_cadColab.comboBox_funcao.addItems (["t","e"])

    frm_cadColab.show()
    App.exec()




