import sqlite3

def retrieve(emp_id):
    conn = sqlite3.connect("./sql/manager_side/sqlite.db",check_same_thread=False)
    leave_info = conn.execute( f'''
    select type,no_of_leaves,reason from manager where emp_id=(?)
    ''',(emp_id,))
    leave_info = leave_info.fetchall()
    # print(leave_info)
    conn.commit()
    conn.close()
    return leave_info

retrieve("U04JMH6NV7Y")