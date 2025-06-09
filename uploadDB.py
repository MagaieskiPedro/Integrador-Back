import sqlite3
import pandas as pd
# ESTE ARQUIVO É RESPONSAVEL PELO UPLOAD DOS DADOS DAS PLANILHAS PARA O BANCO DE DADOS
# Mude para o nome da planilha e edite os nomes dos campos/planilha para bater com o banco de dados

# coloque o nome do arquivo excel que deseja fazer upload em filename
filename="histórico"
# coloque o nome do arquivo de banco de dados em con(conexão) e a extensão de arquivo no arq(arquivo)
con=sqlite3.connect("db.sqlite3")
arq=pd.ExcelFile(filename+'.xlsx')

for sheet in arq.sheet_names:
        # le a planilha do excel e armazena em df(dataframe)
        df=pd.read_excel(filename+'.xlsx',sheet_name=sheet)
        # use append para não sobreescrever a definição (CREATE) do banco
        df.to_sql(sheet,con, index=False,if_exists="append")
#confirma mudanças e fecha os arquivos
con.commit()
con.close()