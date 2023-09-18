import sqlite3
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QPixmap
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import pandas as pd
tabela = pd.read_excel(f'.\dados\cidades.xls')
cidade = tabela.loc[tabela["UF"]=="RS"]
uf = tabela.loc[tabela["UF"]=="RS"]
tabelaf = pd.read_excel(r'.\dados\funcoes.xlsx')
id_colab = 0
# Criando o Bando de Dados
banco = sqlite3.connect(r'.\dados\banco_cadastro.db') 
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS cadastro_user (id INTEGER PRIMARY KEY AUTOINCREMENT,nome varchar(100)NOT NULL,login varchar(100)NOT NULL, senha varchar(100)NOT NULL);")
cursor.execute("""CREATE TABLE IF NOT EXISTS cadastro_colaborador ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome_completa varchar(100)NOT NULL, 
        funcao varchar(100)NOT NULL, 
        cpf varchar(100)NOT NULL,
        rg varchar(100), 
        cnh varchar(100), 
        endereco varchar(100),
        numero varchar(10), 
        bairro varchar(100), 
        cidade varchar(100), 
        uf varchar(2));""")
cursor.execute(f"SELECT * FROM cadastro_user where login='adm';")
nome = cursor.fetchall()
nome_ = len(nome)
if nome_ == 0:
    cursor.execute("INSERT INTO cadastro_user VALUES(1, 'administrador', 'adm', 'adm');")
banco.commit()
def selecionar_colab():
    linha = frm_pesquisarColab.listWidget.currentRow()
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM cadastro_colaborador")
    dados_lidos = cursor.fetchall()
    banco.commit()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM cadastro_colaborador WHERE id="+str(valor_id))
    colab = cursor.fetchall()
    frm_pesquisarColab.close()
    frm_registro.show()
    frm_registro.edt_nome.setText(str(colab[0][1]))

def chamapesquisar2():
    # Conecte-se ao banco de dados e execute a consulta
    banco = sqlite3.connect(r'.\dados\banco_cadastro.db') 
    cursor = banco.cursor()
    cursor.execute("select * from cadastro_colaborador")
    banco.commit()
    dados = cursor.fetchall()

    def filtrar_itens():
        texto_filtro = frm_pesquisarColab.edt_pesquisar.text().lower()
        for i in range(frm_pesquisarColab.listWidget.count()):
            item = frm_pesquisarColab.listWidget.item(i)
            item.setHidden(texto_filtro not in item.text().lower())

    frm_pesquisarColab = uic.loadUi(r'.\frms\frm_pesquisarColabRegistro2.ui')
    
    # Adicione os dados ao listWidget
    for i in range(len(dados)):
        item = QtWidgets.QListWidgetItem(f"{dados[i][1]} - {dados[i][2]}")
        frm_pesquisarColab.listWidget.addItem(item)
    
    frm_pesquisarColab.edt_pesquisar.textChanged.connect(filtrar_itens)
    frm_pesquisarColab.show()

if __name__ == '__main__':
    App = QtWidgets.QApplication([])
    frm_inicial = uic.loadUi(r'.\frms\frm_principal.ui')
    frm_registro = uic.loadUi(r'.\frms\frm_registros.ui')
    frm_pesquisarColab = uic.loadUi(r'.\frms\frm_pesquisarColabRegistro2.ui')
    
    frm_pesquisarColab.btn_selecionar.clicked.connect(selecionar_colab)


    frm_inicial.actionPesquisar.triggered.connect(chamapesquisar2)
    frm_inicial.label.setPixmap(QPixmap(r'.\logo\do-utilizador.png'))
    frm_inicial.label.resize(520,550)
    frm_inicial.show()
    App.exec()
