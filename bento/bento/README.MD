# Oficina Database Management
## This project uses SQLite3 to create, manage and manipulate a database called oficina.db.
### The database is designed to store information related to cars, tools and employees of a workshop.
-----------------------------------------------------------------------------


FIRST STEPS

import sqlite3  

#Absolute path to the database
path_db = r'C:\Users\ba2423\Downloads\bento\db\oficina.db'

#Database connection
connection = sqlite3.connect(path_db)
cursor = connection.cursor()

**CODE**

#Close the connection to the database
connection.close()

---
## Project structure

Tables in the workshop database |
The database contains the following tables: 


Columns:

* id (INTEGER, primary key, auto-increment)
BRAND (TEXT, not null)
cars

* id (INTEGER, primary key, auto-increment)
TOOLS (TEXT, not null)
tools

* id (INTEGER, primary key, auto-increment)
NAMES (TEXT, not null) employees


-----------------------------------------------------------------------------


# Functionalities
Database creation and configuration
Connection to the oficina.db file:

* The file is created automatically if it doesn't exist.
Creation of the cars, tools and employees tables.
Data manipulation
Inserting data:

**Add a brand to the cars table.

**Add a tool to the tools table.

**Add an employee to the employees table.

* Data Query:_

**List all records in all tables.

# Query the cars table
cursor.execute('SELECT * FROM cars') # select the cars table
results = cursor.fetchall() # select all rows
print(“CARS table:”) # print “CARS tables:”
for row in results: # loop for printing the rows until they run out
    print(row)


* Data Selection:_

**Delete all records from all tables.

cursor.execute('DELETE FROM cars') # Delete all data from the 'cars' table
cursor.execute('DELETE FROM tools') # Delete all data from the 'tools' table
cursor.execute('DELETE FROM employees') # Delete all data from the 'employees' table


-----------------------------------------------------------------------------

# How to execute
**Requirements:**

Python 3.x installed.
sqlite3 library (included by default in Python).

* Steps:_

Clone the repository or copy the files to a local directory.
Change the absolute path of the database (path_db) to match the location where the database will be stored.

**Execution

Run the Python scripts to create the database and perform operations:

**create.py: Creates the database tables.

**delete.py: Deletes all the data from the tables.

**sele.py and insert.py: Allows you to insert data and query existing records.

* File Details

**create.py:**
Creates the database and the tables cars, tools and employees.

**delete.py:**
Removes all records from the tables.

**sele.py and insert.py:**
Allows you to:

Insert new makes, tools and employees.
Consult the data in each table.


* Example of Use

**Insert Data**

* When you run insert.py, you'll be asked to enter information: _


**Enter the brand name: Toyota**
Brand 'Toyota' inserted successfully!

**Enter tool name: Wrench**
Tool 'Wrench' inserted successfully!

**Enter employee name: João**
Employee 'John' entered successfully!

**consult data**

* When running sele.py, the following information will be displayed: _

**Consult Data**

_the data will be displayed:_

**CARS table
(1, 'Toyota')

**TOOLS table:**
(1, 'Wrench')

**TABLE EMPLOYEES:**
(1, 'John')

-----------------------------------------------------------------------------
* Notes

Make sure that the path to the oficina.db file is valid before running the scripts.
To change the scripts or add new functionalities, edit the Python files as necessary. 

Translated with DeepL.com (free version)
