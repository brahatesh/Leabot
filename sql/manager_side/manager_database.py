import sqlite3
conn = sqlite3.connect("sqlite.db")

conn.execute('''
Create table manager (
    ref_id VARCHAR(100),
    employee_id VARCHAR(100),
    type VARCHAR(100),
    days_no INT,
    reason VARCHAR(200)
)
''')
conn.close()