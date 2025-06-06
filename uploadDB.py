import sqlite3
import pandas as pd
# Mude para o nome da planilha e edite os nomes dos campos/planilha para bater com o banco de dados
filename="histórico"
con=sqlite3.connect("db.sqlite3")
wb=pd.ExcelFile(filename+'.xlsx')
for sheet in wb.sheet_names:
        df=pd.read_excel(filename+'.xlsx',sheet_name=sheet)
        # append para não sobreescrever a definição (CREATE) do banco
        df.to_sql(sheet,con, index=False,if_exists="append")
# cur = con.cursor()
# con.execute("ALTER TABLE app_ambiente ADD PRIMARY KEY (id)")
con.commit()
con.close()