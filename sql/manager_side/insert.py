import sqlite3

def insert(ref_id,employee_id,type,no_of_leaves,reason):
    conn = sqlite3.connect("./sql/manager_side/sqlite.db")
    params = (ref_id,employee_id,type,no_of_leaves,reason)
    conn.execute( f'''
    insert into manager (ref_id,emp_id,type,no_of_leaves,reason) VALUES
    (?,?,?,?,?)
    ''',params)
    conn.commit()
    conn.close()

insert("456","U04JMH6NV7Y","sick",1,"fever")

