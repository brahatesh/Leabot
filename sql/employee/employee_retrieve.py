import sqlite3

def retrieve(emp_id):
     conn = sqlite3.connect(".\sql\employee\sqlite.db",check_same_thread=False)
     emp_inf =conn.execute( f'''
     select emp_name,emp_leaves from employee1 where emp_id=(?)
    ''',(emp_id,))
     emp_inf =emp_inf.fetchone()
    #  print(emp_inf)
     conn.commit()
     conn.close()



retrieve("U04JMH6NV7Y")
