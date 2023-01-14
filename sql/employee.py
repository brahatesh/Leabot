import sqlite3
## inserting values in employee database
def emp_insert(emp_id,emp_name,emp_leaves):
    conn = sqlite3.connect(".\sql\employee.db")
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

## updating values in employee database
def emp_update(emp_id,no_of_leaves):
    conn = sqlite3.connect(".\sql\employee.db",check_same_thread=False)
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
## retrieving value from employee database
def emp_retrieve(emp_id):
     conn = sqlite3.connect(".\sql\employee.db",check_same_thread=False)
     emp_inf =conn.execute( f'''
     select emp_name,emp_leaves from employee1 where emp_id=(?)
    ''',(emp_id,))
     emp_inf =emp_inf.fetchone()
    #  print(emp_inf)
     conn.commit()
     conn.close()
     return emp_inf



