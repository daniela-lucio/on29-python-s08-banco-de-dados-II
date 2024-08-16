#  **Importação de CSV para SQLite**:
#    - Crie um script que leia um arquivo CSV chamado `clientes.csv` e 
# insira os dados em uma tabela `clientes` no banco de dados SQLite `empresa.db`. 
# A tabela deve ter as colunas `id`, `nome`, `email`.

# import sqlite3
# import csv

# conn = sqlite3.connect('empresa.db')
# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS clientes (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome TEXT NOT NULL,
#     email TEXT NOT NULL
#    )
#    """)

# with open('clientes.csv', newline='', encoding='utf-8') as csvfile:
#     leitor = csv.reader(csvfile)
#     next(leitor)  # Pular o cabeçalho
#     for linha in leitor:
#         cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (linha[1], linha[2]))

# conn.commit()
# cursor.close()
# conn.close()


# 10. **Exportação de SQLite para CSV**:
#     - Escreva um script que exporte os dados da tabela `clientes` do banco de dados `empresa.db` para um arquivo CSV chamado `exportados_clientes.csv`.

import sqlite3
import csv 

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM clientes")
dados = cursor.fetchall()

with open('exportados_clientes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'nome', 'email'])
    escritor.writerows(dados)

cursor.close()
conn.close()