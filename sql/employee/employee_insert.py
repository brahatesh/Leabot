import sqlite3
conn = sqlite3.connect(".\sql\employee\sqlite.db")

def insert(emp_id,emp_name,emp_leaves):
    params = (emp_id,emp_name,emp_leaves)
    f'''
    insert into employee1 (emp_id,emp_name,emp_leaves) VALUES
    (?,?,?)
    '''
    conn.execute( f'''
    insert into employee1 (emp_id,emp_name,emp_leaves) VALUES
    (?,?,?)
    ''',params)
    conn.commit()
    conn.close()


insert("U04JMH6NV7Y","Brahatesh",18)