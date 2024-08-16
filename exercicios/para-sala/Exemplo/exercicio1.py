# import sqlite3
# conn = sqlite3.connect("exemplo.db")
# cursor = conn.cursor()
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS usuarios(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome TEXT NOT NULL,
#     idade INTEGER NOT NULL
#     )
#     """)

# cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('joao', 43)")
# cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('kiko', 89)")

# cursor.execute("SELECT * FROM usuarios")
# registros = cursor.fetchall()

# for registro in registros:
#     print(registros)

# conn.commit()
# conn.close()

# 1. **Criação de Banco de Dados e Tabelas**
#  - Crie um script Python que crie um banco de dados SQLite chamado `escola.db`. 
# Em seguida, crie uma tabela chamada `estudantes` 
# com as colunas `id` (INTEGER, chave primária, autoincremento), `nome` (TEXT) e `idade` (INTEGER).

# import sqlite3

# conn = sqlite3.connect('escola.db')
# cursor = conn.cursor()

# cursor.execute("""
#    CREATE TABLE IF NOT EXISTS estudantes (
#        id INTEGER PRIMARY KEY AUTOINCREMENT,
#        nome TEXT NOT NULL,
#        idade INTEGER NOT NULL
#    )
#    """)

# 2. **Inserção de Dados**:
#    - Escreva um script que insira três registros na tabela `estudantes`.

# import sqlite3
# conn = sqlite3.connect('escola.db')
# cursor = conn.cursor()

# estudantes = [
#     ('Alice', 21),
#     ('Bob', 22),
#     ('Charlie', 23)
#    ]

# cursor.executemany("INSERT INTO estudantes (nome, idade) VALUES (?, ?)", estudantes)

# conn.commit()
# cursor.close()
# conn.close()

# 3. **Consulta de Dados**:
#    - Crie um script que selecione e exiba todos os registros da tabela `estudantes`.

# import sqlite3
# conn = sqlite3.connect('escola.db')
# cursor = conn.cursor()

# cursor.execute("SELECT * FROM estudantes")
# registros = cursor.fetchall()

# for registro in registros:
#     print(registro)

# cursor.close()
# conn.close()

# **Atualização de Dados**:
#    - Escreva um script que atualize a idade de um estudante específico (por exemplo, mude a idade de "Bob" para 23).

# import sqlite3
# conn = sqlite3.connect('escola.db')
# cursor = conn.cursor()

# cursor.execute("UPDATE estudantes SET idade = ? WHERE nome = ?", (23, 'Bob'))

# conn.commit()
# cursor.close()
# conn.close()


# 5. **Remoção de Dados**:
#    - Crie um script que remova um estudante específico (por exemplo, remova "Charlie").

# import sqlite3
# conn = sqlite3.connect('escola.db')
# cursor = conn.cursor()

# cursor.execute("DELETE FROM estudantes WHERE nome = ?", ('Charlie',))

# conn.commit()
# cursor.close()
# conn.close()

# 6. **Consulta com Condições**:
#    - Escreva um script que selecione e exiba todos os estudantes cuja idade seja maior que 21.

import sqlite3
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM estudantes WHERE idade > 21")
registros = cursor.fetchall()

for registro in registros:
    print(registro)

cursor.close()
conn.close()