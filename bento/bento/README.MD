# Oficina Database Management
## Este projeto usa SQLite3 para criar, gerir e manipular uma base de dados chamada oficina.db.
### A base de dados foi concebida para armazenar informação relacionada com carros, ferramentas e empregados de uma oficina.
-----------------------------------------------------------------------------


PRIMEIROS PASSOS

import sqlite3  

#Caminho absoluto para a base de dados
path_db = r'C:\Users\ba2423\Downloads\bento\db\oficina.db'

#Ligação à base de dados
conexão = sqlite3.connect(caminho_db)
cursor = connection.cursor()

**CODE**

#Fechar a ligação à base de dados
connection.close()

---
## Estrutura do projeto

Tabelas na base de dados da oficina
A base de dados contém as seguintes tabelas: 


Colunas:

* id (INTEGER, chave primária, auto-incremento)
MARCA (TEXTO, não nulo)
carros

* id (INTEGER, chave primária, auto-incremento)
TOOLS (TEXT, não nulo)
ferramentas

* id (INTEGER, chave primária, auto-incremento)
NAMES (TEXT, não nulo) empregados


-----------------------------------------------------------------------------


# Funcionalidades
Criação e configuração da base de dados
Ligação ao ficheiro oficina.db:

* O ficheiro é criado automaticamente caso não exista.
Criação das tabelas de carros, ferramentas e empregados.
Manipulação de dados
Inserção de dados:

**Adicionar uma marca à tabela de carros.

**Adicionar uma ferramenta à tabela de ferramentas.

**Inserir um empregado na tabela de empregados.

* Consulta de dados:_.

**Listar todos os registos em todas as tabelas.

# Consultar a tabela carros
cursor.execute('SELECT * FROM cars') # seleciona a tabela cars
results = cursor.fetchall() # seleciona todas as linhas
print(“CARS table:”) # print “CARS tables:”
for row in results: # loop for printing the rows until they run out
    print(row)


* Seleção de dados:_

**Eliminar todos os registos de todas as tabelas.

cursor.execute('DELETE FROM cars') # Apaga todos os dados da tabela 'cars'
cursor.execute('DELETE FROM tools') # Apaga todos os dados da tabela 'tools'
cursor.execute('DELETE FROM employees') # Apaga todos os dados da tabela 'employees'


-----------------------------------------------------------------------------

# Como executar
**Requisitos

Python 3.x instalado.
Biblioteca sqlite3 (incluída por padrão no Python).

* Passos:_

Clonar o repositório ou copiar os ficheiros para um diretório local.
Alterar o caminho absoluto da base de dados (path_db) para corresponder ao local onde a base de dados será armazenada.

**Execução

Execute os scripts Python para criar a base de dados e efetuar operações:

**create.py: Cria as tabelas do banco de dados.

**delete.py: Apaga todos os dados das tabelas.

**sele.py e insert.py: Permite inserir dados e consultar registos existentes.

* Detalhes do ficheiro

**create.py:**
Cria a base de dados e as tabelas carros, ferramentas e empregados.

**delete.py:**
Remove todos os registos das tabelas.

**sele.py e insert.py:**
Permite-lhe:

Inserir novas marcas, ferramentas e funcionários.
Consultar os dados de cada tabela.


* Exemplo de Utilização

**Inserir Dados**

* Ao executar o insert.py, ser-lhe-á pedido para introduzir informação: _


**Introduza o nome da marca: Toyota**
Marca 'Toyota' inserida com sucesso!

**Introduzir o nome da ferramenta: Wrench**
Ferramenta 'Wrench' inserida com sucesso!

**Entrar o nome do empregado: João**
Funcionário 'João' inserido com sucesso!

**consultar dados**

* Ao executar o sele.py, as seguintes informações serão exibidas: _

**Dados da consulta**

_os dados serão apresentados:_

**Tabela CARROS
(1, 'Toyota')

**Tabela de ferramentas:**
(1, 'Wrench')

**TABELA EMPREGADOS:**
(1, 'João')

-----------------------------------------------------------------------------
* Notas

Certifique-se de que o caminho para o ficheiro oficina.db é válido antes de executar os scripts.
Para alterar os scripts ou adicionar novas funcionalidades, edite os ficheiros Python conforme necessário. 


Traduzido com a versão gratuita do tradutor - DeepL.com
