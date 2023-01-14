import sqlite3

def retrieve(ref_id):
    conn = sqlite3.connect("./sql/manager_side/sqlite.db",check_same_thread=False)
    leave_info = conn.execute( f'''
    select employee_id,type,no_of_leaves,reason from manager where ref_id=(?)
    ''',(ref_id,))
    leave_info = leave_info.fetchone()
    print (leave_info)
    conn.commit()
    conn.close()
