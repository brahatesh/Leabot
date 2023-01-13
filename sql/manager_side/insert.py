import sqlite3
conn = sqlite3.connect("sqlite.db")

ins='''
insert into manager (employee_id,type,days_no,reason) VALUES
('','12th')
'''

conn.execute(ins)
conn.commit()
conn.close()