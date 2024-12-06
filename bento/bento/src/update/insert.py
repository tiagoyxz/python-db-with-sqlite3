import sqlite3 #IMPORTA BIBLIOTECA

#CAMINHO PARA A DATABASE
caminho_db = r'C:\Users\ba2423\Downloads\bento\bento\db\oficina.db'

#CONEXÃO
conexao = sqlite3.connect(caminho_db)
#CURSOR PARA FAZER A CONEXÃO
cursor = conexao.cursor()

#FUNÇÃO PARA INSERIR DADOS NA TABELA CARROS
def inserir_marca(marca):
    cursor.execute('INSERT INTO carros (MARCA) VALUES (?)', (marca,))
    conexao.commit()
    print(f"Marca '{marca}' inserida com sucesso!")

#INSERIR A MARCA
nome_marca = input("Digite o nome da marca: ")
inserir_marca(nome_marca)

#CONSULTAR DADOS DA TABLE CARROS
cursor.execute('SELECT * FROM carros')
#SELECIONA TODOS OS RESULTADOS
resultados = cursor.fetchall()
#IMPRIME TODOS OS RESULTADOS
print("\nTabela CARROS:")
for linha in resultados:
    print(linha)


def inserir_ferramenta(ferramenta):
    cursor.execute('INSERT INTO ferramentas (FERRAMENTAS) VALUES (?)', (ferramenta,))
    conexao.commit()
    print(f"Ferramenta '{ferramenta}' inserida com sucesso!")


nome_ferramenta = input("\nDigite o nome da ferramenta: ")
inserir_ferramenta(nome_ferramenta)

#CONSULTAR DA TABELA FERRAMENTAS
cursor.execute('SELECT * FROM ferramentas')
resultados = cursor.fetchall()
print("\nTabela FERRAMENTAS:")
for linha in resultados:
    print(linha)

# Função para inserir um funcionário na tabela funcionarios
def inserir_funcionario(nome):
    cursor.execute('INSERT INTO funcionarios (NOMES) VALUES (?)', (nome,))
    conexao.commit()
    print(f"Funcionário '{nome}' inserido com sucesso!")

# Inserindo um novo funcionário
nome_funcionario = input("\nDigite o nome do funcionário: ")
inserir_funcionario(nome_funcionario)

# Consultar a tabela funcionarios
cursor.execute('SELECT * FROM funcionarios')
resultados = cursor.fetchall()
print("\nTabela FUNCIONARIOS:")
for linha in resultados:
    print(linha)

# Fechar a conexão com o banco de dados
conexao.close()
