import sqlite3
conn = sqlite3.connect("sqlite.db")

ins='''
insert into employee (emp_id,emp_name,emp_leaves) VALUES
('U04JMH6NV7Y','Brahatesh',18)
'''

conn.execute(ins)
conn.commit()
conn.close()