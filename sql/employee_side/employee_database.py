import sqlite3
conn = sqlite3.connect("sqlite.db")
conn.execute('''
Create table employee (
    emp_id VARCHAR(100)  PRIMARY KEY,
    emp_name VARCHAR(50),
    emp_leaves int
)
''')
conn.close()