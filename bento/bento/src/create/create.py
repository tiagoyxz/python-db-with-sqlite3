import sqlite3 #IMPORTA BIBLIOTECA

#CAMINHO PARA A DATABASE
caminho_db = r'C:\Users\ba2423\Downloads\bento\bento\db\oficina.db'

#CONEXÃO
conexao = sqlite3.connect(caminho_db)
#CURSOR PARA FAZER A CONEXÃO
cursor = conexao.cursor()

#----------------------------------------------------------------------------------------

#CRIAÇÃO DA TABELA CARROS COM CURSOR.EXECUTE
# "id INTEGER PRIMARY KEY AUTOINCREMENT," OBRIGATORIO COLOCAR DADOS NO ID
# "MARCA TEXT NOT NULL" COLUNA MARCA TEM QUE TER DADOS E O TIPO DE DADOS É TEXTO
cursor.execute('''  
CREATE TABLE IF NOT EXISTS carros (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    MARCA TEXT NOT NULL
)
''')

cursor.execute('''  
CREATE TABLE IF NOT EXISTS ferramentas (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    FERRAMENTAS TEXT NOT NULL
)
''')

cursor.execute('''  
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    NOMES TEXT NOT NULL
)
''')
#----------------------------------------------------------------------------------------

# SALVAR DADOS
conexao.commit()

#----------------------------------------------------------------------------------------

# SELECIONA DA TABELA "CARROS"
cursor.execute('SELECT * FROM carros')
# SELECIONA OS RESULTADOS TODOS
resultados = cursor.fetchall()
# IMPRIME OS RESULTADOS
print(resultados) 

#----------------------------------------------------------------------------------------

# FECHA A CONEXÃO COM A BASE DE DADOS
conexao.close()
