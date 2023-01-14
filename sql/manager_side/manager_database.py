import sqlite3
conn = sqlite3.connect("./sql/manager_side/sqlite.db")

conn.execute('''
Create table manager (
    ref_id VARCHAR(100) PRIMARY KEY,
    employee_id text,
    type VARCHAR(100),
    no_of_leaves INT,
    reason VARCHAR(200)
)
''')
conn.close()