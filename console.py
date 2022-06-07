#from email.utils import collapse_rfc2231_value
import os
import sqlite3
from PyQt5 import uic, QtWidgets, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import pandas as pd
tabela = pd.read_excel(f'.\dados\cidades.xls')
cidade = tabela.loc[tabela["UF"]=="RS"]
uf = tabela.loc[tabela["UF"]=="RS"]
tabelaf = pd.read_excel(r'.\dados\funcoes.xlsx')
id_colab = 0
# Criando o Bando de Dados
banco = sqlite3.connect('banco_cadastro.db') 
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
def cadastro_colaborador():
    id = frm_cadColab.edt_id.text()
    nomecompleto = frm_cadColab.edt_nome.text()
    funcao = frm_cadColab.comboBox_funcao.currentText()
    cpf = frm_cadColab.edt_cpf.text()
    rg = frm_cadColab.edt_rg.text()
    cnh = frm_cadColab.edt_cnh.text()
    endereco = frm_cadColab.edt_endereco.text()
    numero = frm_cadColab.edt_numeroEnd.text()
    bairro = frm_cadColab.edt_bairro.text()
    cidade = frm_cadColab.comboBox_cidade.currentText()
    uf = frm_cadColab.comboBox_uf.currentText()
    try:
        banco = sqlite3.connect('banco_cadastro.db') 
        cursor = banco.cursor()
        # cria o bando se ele nao exixtir 
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
        # verifica se o colaborador já existe 
        if id == "":
            # inserir dados na tabela
            cursor.execute("INSERT INTO cadastro_colaborador VALUES(NULL,'"+nomecompleto+"','"+funcao+"','"+cpf+"','"+rg+"','"+cnh+"','"+endereco+"','"+numero+"','"+bairro+"','"+cidade+"','"+uf+"')")
            banco.commit()
            banco.close()
            frm_cadColab.edt_nome.setText('')
            frm_cadColab.edt_cpf.setText('')
            frm_cadColab.edt_rg.setText('')
            frm_cadColab.edt_cnh.setText('')
            frm_cadColab.edt_endereco.setText('')           
            QMessageBox.information(frm_cadColab, "Aviso", "Colaborador cadastrado com sucesso")
        else:
            cursor.execute("UPDATE cadastro_colaborador SET nome_completa = '"+nomecompleto+"', funcao = '"+funcao+"',cpf = '"+cpf+"', rg = '"+rg+"', cnh = '"+cnh+"', endereco = '"+endereco+"', numero = '"+numero+"', bairro = '"+endereco+"', cidade = '"+cidade+"', uf = '"+uf+"' WHERE id = '"+id+"'")
            banco.commit()
            banco.close()
            frm_cadColab.edt_nome.setText('')
            frm_cadColab.edt_cpf.setText('')
            frm_cadColab.edt_rg.setText('')
            frm_cadColab.edt_cnh.setText('')
            frm_cadColab.edt_endereco.setText('')
            frm_cadColab.close()
            frm_pesquisarColab.show()
            QMessageBox.information(frm_cadColab, "Aviso", "Colaborador atualizado com sucesso")
    except sqlite3.Error as erro:
        print("Erro ao inserir os dados: ",erro)
        QMessageBox.about(frm_cadColab, "ERRO","Erro ao inserir os dados")
        banco.close()   
def funcao_login():
    nome_user = frm_login.lineuser.text()
    key = frm_login.linekey.text()
    cursor.execute(f"SELECT senha FROM cadastro_user where login='{nome_user}';")
    senha_db = cursor.fetchall()
    if key == senha_db[0][0]:
        frm_login.close()
        frm_inicial.show()
    else:
        QMessageBox.about(frm_login, "Erro", "Usuário ou senha invalido!")
        frm_login.linekey.setText('')
        frm_login.lineuser.setText('')
    banco.commit()
    banco.close()
def cadastro_user():
    nome = frm_cadUser.edt_nome.text()
    login = frm_cadUser.edt_login.text()
    senha = frm_cadUser.edt_senha.text()
    c_senha = frm_cadUser.edt_c_senha.text()
    if login != "" and nome != "" and senha != "":
        if (senha == c_senha):
            try:
                banco = sqlite3.connect('banco_cadastro.db')
                cursor = banco.cursor()
                cursor.execute("INSERT INTO cadastro_user VALUES (NULL,'"+nome+"','"+login+"','"+senha+"');")
                banco.commit()
                banco.close()
                QMessageBox.information(frm_cadUser, "Aviso", "Usuario cadastrado com sucesso")
            except sqlite3.Error as erro:
                QMessageBox.about(frm_cadUser, "ERRO","Erro ao inserir os dados: ",erro)
        else:
            QMessageBox.about(frm_cadUser,"ERRO", "As senhas digitadas estão diferentes")
    else:
        QMessageBox.about(frm_cadUser,"ERRO", "digite os dados!")
def cadastra_funcao():
    descs = str(frm_funcao.edt_funcao.text())
    tabelaf = pd.read_excel(r'.\dados\funcoes.xlsx')
    tabelaf= tabelaf.append({'descricao': descs}, ignore_index=True)
    tabelaf.to_excel(r'.\dados\funcoes.xlsx', index = False)
    frm_funcao.edt_funcao.setText("")
def chamacadastrouser():
    frm_cadUser.show()
    frm_inicial.close()
def chamatelainicial():
    frm_cadUser.close()
    frm_inicial.show()
def chamapesquisar():
    cursor.execute("SELECT * FROM cadastro_colaborador")
    dados_lidos = cursor.fetchall()
    banco.commit()
    frm_pesquisarColab.tableWidget.setRowCount(len(dados_lidos))
    frm_pesquisarColab.tableWidget.setColumnCount(10)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 10):
           frm_pesquisarColab.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    frm_pesquisarColab.show()
def chamatabelas():
    try:
        banco = sqlite3.connect('banco_cadastro.db') 
        cursor = banco.cursor()
        cursor.execute("select * from tabela")
        dados_lidos = cursor.fetchall()
        frm_tabela.edt_diaria.setText(str('%.2f'%dados_lidos[0][1]).replace('.',','))
        frm_tabela.edt_hextra.setText(str('%.2f'%dados_lidos[0][2]).replace('.',','))
        frm_tabela.edt_vtransp.setText(str('%.2f'%dados_lidos[0][3]).replace('.',','))
        frm_tabela.edt_vref.setText(str('%.2f'%dados_lidos[0][4]).replace('.',','))
    except sqlite3.Error as erro:
        print("Erro ao inserir os dados: ",erro)
    frm_tabela.show()
def pesquisar_colab():
    pass
def salvaregistro():
    pass
def editar_colab():
    global id_colab
    linha =frm_pesquisarColab.tableWidget.currentRow()
    cursor.execute("SELECT * FROM cadastro_colaborador")
    dados_lidos = cursor.fetchall()
    banco.commit()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM cadastro_colaborador WHERE id="+str(valor_id))
    colab = cursor.fetchall()
    frm_cadColab.edt_id.setText(str(colab[0][0]))
    frm_cadColab.edt_nome.setText(colab[0][1])
    frm_cadColab.comboBox_funcao.addItem(colab[0][2])
    frm_cadColab.edt_cpf.setText(colab[0][3])
    frm_cadColab.edt_rg.setText(colab[0][4])
    frm_cadColab.edt_cnh.setText(colab[0][5])
    frm_cadColab.edt_endereco.setText(colab[0][6])
    frm_cadColab.edt_numeroEnd.setText(colab[0][7])
    frm_cadColab.edt_bairro.setText(colab[0][8])
    frm_cadColab.comboBox_cidade.addItem(str(colab[0][9]))
    frm_cadColab.comboBox_uf.addItem(colab[0][10])
    id_colab = valor_id
    frm_cadColab.show()
def chamacadColab():
    frm_cadColab.show()
def fechacolab():
    frm_cadColab.close()
    tabelaf = pd.read_excel(r'.\dados\funcoes.xlsx')
def chamacadfuncao():
    frm_funcao.show()
    frm_funcao.edt_funcao.setText("")
def salvar_tabela():
    diaria = float(frm_tabela.edt_diaria.text().replace(',','.')) # 85,00
    hextra = float(frm_tabela.edt_hextra.text().replace(',','.')) # 16,00
    vtrans = float(frm_tabela.edt_vtransp.text().replace(',','.')) # 12,30
    vresf = float(frm_tabela.edt_vref.text().replace(',','.')) # 17,00
    try:
        banco = sqlite3.connect('banco_cadastro.db') 
        cursor = banco.cursor()
        # cria o bando se ele nao exixtir 
        cursor.execute("""CREATE TABLE IF NOT EXISTS tabela ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        diaria decimal(5,2) NOT NULL, 
        hextra decimal(5,2) NOT NULL, 
        vtransp decimal(5,2) NOT NULL,
        vref decimal(5,2) NOT NULL);""")
        cursor.execute("select * from tabela")
        dados = cursor.fetchall()
        tables = len(dados)
        if tables == 0:
            # inserir dados na tabela
            cursor.execute("INSERT INTO tabela VALUES(NULL,'"+diaria+"','"+hextra+"','"+vtrans+"','"+vresf+"')")
            banco.commit()
            banco.close()
            frm_tabela.edt_diaria.setText('')
            frm_tabela.edt_hextra.setText('')
            frm_tabela.edt_vtransp.setText('')
            frm_tabela.edt_vref.setText('')
            QMessageBox.information(frm_tabela, "Aviso", "Tabela cadastrado com sucesso")
        else:
            cursor.execute("UPDATE tabela SET diaria = '"+diaria+"', hextra = '"+hextra+"',vtransp = '"+vtrans+"', vref = '"+vresf+"'")
            banco.commit()
            banco.close()
            frm_tabela.edt_diaria.setText('')
            frm_tabela.edt_hextra.setText('')
            frm_tabela.edt_vtransp.setText('')
            frm_tabela.edt_vref.setText('')
            QMessageBox.information(frm_tabela, "Aviso", "Tabela atualizado com sucesso")
    except sqlite3.Error as erro:
        print("Erro ao inserir os dados: ",erro)
        QMessageBox.about(frm_tabela, "ERRO","Erro ao inserir os dados")
        banco.close()
def chamaregistro():
    try:
        banco = sqlite3.connect('banco_cadastro.db') 
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM tabela")
        dados_lidos = cursor.fetchall()
        tables = len(dados_lidos)
        banco.commit()
        banco.close()
        if tables == 0:
            frm_registro.edt_diaria.setText('')
            frm_registro.edt_hextra.setText('')
            frm_registro.edt_vtransp.setText('')
            frm_registro.edt_vref.setText('')
        else:
            frm_registro.edt_diaria.setText(str('%.2f'%dados_lidos[0][1]).replace('.',','))
            frm_registro.edt_hextra.setText(str('%.2f'%dados_lidos[0][2]).replace('.',','))
            frm_registro.edt_vtransp.setText(str('%.2f'%dados_lidos[0][3]).replace('.',','))
            frm_registro.edt_vref.setText(str('%.2f'%dados_lidos[0][4]).replace('.',','))
    except sqlite3.Error as erro:
        print("Erro ao inserir os dados: ",erro) 
    frm_registro.show()
if __name__ == '__main__':
    App = QtWidgets.QApplication([])
    frm_inicial = uic.loadUi(r'.\frms\frm_principal.ui')
    frm_cadColab = uic.loadUi(r'.\frms\frm_cadastroColab.ui')
    frm_cadUser = uic.loadUi(r'.\frms\frm_cadastroUser.ui')
    frm_pesquisarColab = uic.loadUi(r'.\frms\frm_pesquisarColab.ui')
    frm_login = uic.loadUi(r'.\frms\frm_login.ui')
    frm_funcao = uic.loadUi(r'.\frms\frm_funcao.ui')
    frm_tabela = uic.loadUi(r'.\frms\frm_tabelas.ui')
    frm_registro = uic.loadUi(r'.\frms\frm_registros.ui')
    # botões da tela registros
    frm_registro.tbn_salvar.clicked.connect(salvaregistro)
    frm_registro.tbn_pesquisar.clicked.connect(pesquisar_colab)
    # botões da tela tabela
    frm_tabela.btn_salvar.clicked.connect(salvar_tabela)
    # botões da tela cadastro funcao
    frm_funcao.btn_salvar.clicked.connect(cadastra_funcao)
    # botões da tela login
    frm_login.btnlogin.clicked.connect(funcao_login)
    # botões da tela principal 
    frm_inicial.actionUser.triggered.connect(chamacadastrouser)
    frm_inicial.actionCadastrar.triggered.connect(chamacadColab)
    frm_inicial.actionPesquisar.triggered.connect(chamapesquisar)
    frm_inicial.actionCadastrar_Fun.triggered.connect(chamacadfuncao)
    frm_inicial.actionTabelas.triggered.connect(chamatabelas)
    frm_inicial.actionRegistro_Semanal.triggered.connect(chamaregistro)
    frm_inicial.label.setPixmap(QtGui.QPixmap(r'.\logo\do-utilizador.png'))
    frm_inicial.label.resize(520,550)
    # botões da tela cadastro de user
    frm_cadUser.btn_salvar.clicked.connect(cadastro_user)
    frm_cadUser.btn_fechar.clicked.connect(chamatelainicial)
    # botões da tela pesquisar colaborador
    frm_pesquisarColab.btn_pesquisar.clicked.connect(pesquisar_colab)
    frm_pesquisarColab.btn_editar.clicked.connect(editar_colab)
    # botões da tela cadastro colaborador
    frm_cadColab.btn_fechar.clicked.connect(fechacolab)
    frm_cadColab.comboBox_funcao.addItems(tabelaf["descricao"])
    frm_cadColab.comboBox_uf.addItems(uf["UF"])
    frm_cadColab.comboBox_cidade.addItems(cidade["cidade"])
    frm_cadColab.btn_salvar.clicked.connect(cadastro_colaborador)
    frm_inicial.show()
    App.exec()