

import pandas as pd
tabela = pd.read_excel(f'.\dados\cidades.xls')
"""estado = input("digite o estado: ")
print(tabela.loc[tabela["UF"]=="{}".format(estado)])"""


uf_tabela = pd.read_excel(f'.\dados\cidades.xls', index_col= "UF")
cidade_tabela = pd.read_excel(f'.\dados\cidades.xls', index_col= "cidade")
uf = uf_tabela.columns.values
print(uf_tabela.columns.values)

