import sqlite3
conn = sqlite3.connect("sqlite.db")

ins='''
insert into student (st_name,st_class) VALUES
('Shyam','12th')
'''

conn.execute(ins)
conn.commit()
conn.close()