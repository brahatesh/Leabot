import sqlite3
conn = sqlite3.connect("./sql/manager.db")

#Database fields for manager database
def make_db() :
    conn.execute('''
Create table manager (
    ref_id VARCHAR(100) PRIMARY KEY,
    employee_id text,
    type VARCHAR(100),
    no_of_leaves INT,
    reason text,
    channel_id text,
    flag bool 
)
''')
    conn.close()


# Inserting data in manager database
def insert(ref_id,employee_id,type,no_of_leaves,reason,c_id,flag):
    conn = sqlite3.connect("./sql/manager.db")
    params = (ref_id,employee_id,type,no_of_leaves,reason,c_id,flag)
    conn.execute( f'''
    insert into manager (ref_id,employee_id,type,no_of_leaves,reason,channel_id,flag) VALUES
    (?,?,?,?,?,?,?)
    ''',params)
    conn.commit()
    conn.close()

# Function for retrieving data using emp_id as parameter
def retrieve(emp_id):
    conn = sqlite3.connect("./sql/manager.db",check_same_thread=False)
    leave_info = conn.execute( f'''
    select type,no_of_leaves,reason,channel_id,flag from manager where employee_id=(?)
    ''',(emp_id,))
    leave_info = leave_info.fetchall()
    conn.commit()
    conn.close()
    return leave_info

# Function for retrieving data using ref_id as parameter
def retrieve_ref(ref_id):
    conn = sqlite3.connect("./sql/manager.db",check_same_thread=False)
    leave_info = conn.execute( f'''
    select employee_id,type,no_of_leaves,reason,channel_id,flag from manager where ref_id=(?)
    ''',(ref_id,))
    leave_info = leave_info.fetchall()
    conn.commit()
    conn.close()
    return leave_info


def delete_ref(ref_id):
    conn = sqlite3.connect("./sql/manager.db",check_same_thread=False)
    conn.execute( f'''
    DELETE FROM manager WHERE ref_id=(?)
    ''',(ref_id,))
    conn.commit()
    conn.close()

def mutate(ref_id,accepted):
    conn = sqlite3.connect("./sql/manager.db",check_same_thread=False)
    if(accepted):
        conn.execute( f'''
            update manager set flag=1 where ref_id=(?)
        ''',(ref_id,))
    conn.commit()
    conn.close()


