#  - Crie um script Python que crie um banco de dados SQLite chamado `livraria.db`. 
# Em seguida, crie uma tabela chamada `estudantes` 
# com as colunas `id` (INTEGER, chave primária, autoincremento), `nome` (TEXT) e `idade` (INTEGER).

import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        título TEXT NOT NULL,
        autor TEXT NOT NULL,
        ano INTEGER NOT NULL,
        preco REAL NOT NULL,
    )
    """)
conn.commit()
cursor.close()
conn.close()

import csv

with open('livros.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    for linha in leitor:
        print(linha)

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM livros")
registros = cursor.fetchall()

for registro in registros:
    print(registro)

cursor.close()
conn.close()
