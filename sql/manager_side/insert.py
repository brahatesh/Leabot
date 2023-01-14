import sqlite3

def insert(ref_id,employee_id,type,no_of_leaves,reason):
    conn = sqlite3.connect("./sql/manager_side/sqlite.db")
    params = (ref_id,employee_id,type,no_of_leaves,reason)
    conn.execute( f'''
    insert into manager (ref_id,employee_id,type,no_of_leaves,reason) VALUES
    (?,?,?,?,?)
    ''',params)
    conn.commit()
    conn.close()

