import sqlite3

def update(emp_id,no_of_leaves):
    conn = sqlite3.connect(".\sql\employee\sqlite.db",check_same_thread=False)
    curr_leave = conn.execute( f'''
     select emp_leaves from employee1 where emp_id=(?)
    ''',(emp_id,))
    (curr) = curr_leave.fetchone()
    # print(curr)
    rem_leaves = curr[0] - no_of_leaves
    params =(rem_leaves,emp_id)
    conn.execute(f'''
        update employee1 set emp_leaves=(?) where emp_id=(?)
    ''',(params))

    conn.commit()
    conn.close()

