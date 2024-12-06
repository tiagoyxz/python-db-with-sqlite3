import sqlite3  #IMPORTA A BIBLIOTECA SQLITE3

 
# CAMINHO ONDE ESTÁ A BASE DE DADOS
caminho_db = r'C:\Users\ba2423\Downloads\bento\bento\db\oficina.db'

#CONECTA A BASE DE DADOS
conexao = sqlite3.connect(caminho_db)
#CURSOR PARA EXECUTAR A CONEXÃO
cursor = conexao.cursor()

# DELETA DAS TABELAS SELECIONADAS TODOS OS DADOS
cursor.execute('DELETE FROM carros')  # Deleta todos os dados da tabela 'carros'
cursor.execute('DELETE FROM ferramentas')  # Deleta todos os dados da tabela 'ferramentas'
cursor.execute('DELETE FROM funcionarios')  # Deleta todos os dados da tabela 'funcionarios'

# SALVA AS ALTERAÇÕES
conexao.commit()

# FECHA A CONEXÃO
conexao.close()
