import sqlite3  

# Caminho absoluto para o banco de dados
caminho_db = r'C:\Users\ba2423\Downloads\bento\bento\db\oficina.db'

# Conexão com o banco de dados
conexao = sqlite3.connect(caminho_db)
cursor = conexao.cursor()


    # Consultar a tabela carros
cursor.execute("SELECT FROM carros WHERE='Civic' AND id='2'")
resultados = cursor.fetchall()
print("Tabela CARROS:")
for linha in resultados:
    print(linha)

    
# Fechar a conexão com o banco de dados
conexao.close()
