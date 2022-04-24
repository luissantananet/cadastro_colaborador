import os
import sqlite3
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


banco = sqlite3.connect('banco_cadastro.db') 
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text,login text,senha text)")
banco.commit() 
banco.close()

        

def chamacadastrouser():
    tela.principal.close()
    tela.cadastro_usuario.show()
def chamatelainicial():
    tela.cadastro_usuario.close()
    tela.principal.show()
if __name__ == '__main__':
    App = QtWidgets.QApplication([])
    tela = uic.loadUi('frm_principal.ui')
    
    # botões da tela login
     
    # botões da tela principal 
    tela.actionUser.triggered.connect(chamacadastrouser)
    tela.logo.setPixmap(QtGui.QPixmap(r"./logo/logo.png"))
    tela.logo.resize(450,200)
    # botões da tela cadastro de user
    tela.btn_fechar_2.clicked.connect(chamatelainicial)
    tela.show()
    App.exec()