import sqlite3
conn = sqlite3.connect("sqlite.db")
def update(emp_id,no_of_leaves):
    curr_leave = conn.execute( f'''
     select emp_leaves from employee1 where emp_id=(?)
    ''',(emp_id,))
    (curr_leave) = curr_leave.fetchone()
    rem_leaves = curr_leave[0] - no_of_leaves
    params =(rem_leaves,emp_id)
    conn.execute(f'''
        update employee1 set emp_leaves=(?) where emp_id=(?)
    ''',(params))

    conn.commit()
    conn.close()

