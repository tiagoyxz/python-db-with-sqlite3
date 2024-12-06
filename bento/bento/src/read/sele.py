import sqlite3  #IMPORTA BIBLIOTECA

#CAMINHO PARA A DATABASE
caminho_db = r'C:\Users\ba2423\Downloads\bento\bento\db\oficina.db'

#CONEXÃO
conexao = sqlite3.connect(caminho_db)
#CURSOR PARA FAZER A CONEXÃO
cursor = conexao.cursor()

#----------------------------------------------------------------------------------------

#SELECIONA DA TABELA CARROS COM CURSOR.EXECUTE
cursor.execute('SELECT * FROM carros')
#SELECIONA TODOS OS RESULTADOS
resultados = cursor.fetchall()
#IMPRIME TODOS OS RESULTADOS
print("Tabela CARROS:")
for linha in resultados:
    print(linha)


cursor.execute('SELECT * FROM ferramentas')
resultados = cursor.fetchall()
print("\nTabela FERRAMENTAS:")
for linha in resultados:
    print(linha)


cursor.execute('SELECT * FROM funcionarios')
resultados = cursor.fetchall()
print("\nTabela FUNCIONARIOS:")
for linha in resultados:
    print(linha)

#FECHA A CONEXÃO
conexao.close()
