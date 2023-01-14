import sqlite3
conn = sqlite3.connect("./sql/manager_side/sqlite.db")

def insert(ref_id,employee_id,type,no_of_leaves,reason):
    params = (ref_id,employee_id,type,no_of_leaves,reason)
    conn.execute( f'''
    insert into manager (ref_id,employee_id,type,no_of_leaves,reason) VALUES
    (?,?,?,?,?)
    ''',params)
    conn.commit()
    conn.close()


insert("123","U04JMH6NV7Y","sick",2,"got fever")