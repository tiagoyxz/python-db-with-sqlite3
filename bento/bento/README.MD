# Oficina Database Management
## Este projeto utiliza o SQLite3 para criar, gerenciar e manipular um banco de dados chamado oficina.db.
### O banco de dados é projetado para armazenar informações relacionadas a carros, ferramentas e funcionários de uma oficina.
-----------------------------------------------------------------------------


PRIMEIROS PASSOS

import sqlite3  

#Caminho absoluto para o banco de dados
caminho_db = r'C:\Users\ba2423\Downloads\bento\bento\db\oficina.db'

#Conexão com o banco de dados
conexao = sqlite3.connect(caminho_db)
cursor = conexao.cursor()

**CODIGO**

#Fechar a conexão com o banco de dados
conexao.close()

---
##  Estrutura do Projeto

Tabelas no Banco de Dados da oficina |
O banco de dados contém as seguintes tabelas: 


Colunas:

* id (INTEGER, chave primária, auto-incremento)
MARCA (TEXT, não nulo)
carros

* id (INTEGER, chave primária, auto-incremento)
FERRAMENTAS (TEXT, não nulo)
ferramentas

* id (INTEGER, chave primária, auto-incremento)
NOMES (TEXT, não nulo) funcionarios


-----------------------------------------------------------------------------


# Funcionalidades
Criação e Configuração do Banco de Dados
Conexão com o arquivo oficina.db:

* O arquivo é criado automaticamente caso não exista.
Criação das tabelas carros, ferramentas e funcionarios.
Manipulação de Dados
Inserção de Dados:

**Adicionar uma marca à tabela carros.**

**Adicionar uma ferramenta à tabela ferramentas.**

**Adicionar um funcionário à tabela funcionarios.**

* _Consulta de Dados:_

**Listar todos os registros de todas tabelas.**

# Consultar a tabela carros
cursor.execute('SELECT * FROM carros') # seleciona a tabela carros
resultados = cursor.fetchall() # seleciona as linhas todas
print("Tabela CARROS:") # imprime "Tabelas CARROS:"
for linha in resultados: # faz um ciclo for a imprimir as linhas até acabarem
    print(linha)


* _Deleção de Dados:_

**Deletar todos os registros de todas as tabelas.**

cursor.execute('DELETE FROM carros')  # Deleta todos os dados da tabela 'carros'
cursor.execute('DELETE FROM ferramentas')  # Deleta todos os dados da tabela 'ferramentas'
cursor.execute('DELETE FROM funcionarios')  # Deleta todos os dados da tabela 'funcionarios'


-----------------------------------------------------------------------------

# Como Executar
**Requisitos:**

_Python 3.x instalado._
Biblioteca sqlite3 (inclusa por padrão no Python).

* _Passos:_

Clone o repositório ou copie os arquivos para um diretório local.
Altere o caminho absoluto do banco de dados (caminho_db) para corresponder ao local em que o banco será armazenado.

**Execução:**

Rode os scripts Python para criar o banco de dados e realizar operações:

**create.py: Cria as tabelas do banco de dados.**

**delete.py: Deleta todos os dados das tabelas.**

**sele.py e insert.py: Permite inserir dados e consultar os registros existentes.**

* _Detalhes dos Arquivos_

**create.py:**
Cria o banco de dados e as tabelas carros, ferramentas e funcionarios.

**delete.py:**
Remove todos os registros das tabelas.

**sele.py e insert.py:**
Permite:

Inserir novas marcas, ferramentas e funcionários.
Consultar os dados de cada tabela.


* _Exemplo de Uso_

**Inserir Dados**

* _Ao executar insert.py, você será solicitado a inserir informações:_


**Digite o nome da marca: Toyota**
Marca 'Toyota' inserida com sucesso!

**Digite o nome da ferramenta: Chave Inglesa**
Ferramenta 'Chave Inglesa' inserida com sucesso!

**Digite o nome do funcionário: João**
Funcionário 'João' inserido com sucesso!

**consultar dados**

* _Ao executar sele.py, será exibido as informações:_

**Consultar Dados**

_os dados serão exibidos:_

**Tabela CARROS:**
(1, 'Toyota')

**Tabela FERRAMENTAS:**
(1, 'Chave Inglesa')

**Tabela FUNCIONARIOS:**
(1, 'João')

-----------------------------------------------------------------------------
* **_Observações_**

Certifique-se de que o caminho para o arquivo oficina.db é válido antes de executar os scripts.
Para alterar os scripts ou adicionar novas funcionalidades, edite os arquivos Python conforme necessário. 