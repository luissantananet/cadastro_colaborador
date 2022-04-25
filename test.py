import sqlite3

banco = sqlite3.connect('banco_cadastro.db') 
cursor = banco.cursor()

nome_user = 'adm'
key = 'adm'

#cursor = banco.cursor()
cursor.execute(f"SELECT * FROM cadastro_user where login='{nome_user}';")
senha_db = cursor.fetchall()
nome = len(senha_db)

if nome == 0:
    print(nome)
    cursor.execute("INSERT INTO cadastro_user VALUES(1, 'administrador', 'adm', 'adm');")
else:
    print("diferente de 0")