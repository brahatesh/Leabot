import sqlite3
conn = sqlite3.connect("./sql/manager.db")

# Database fields for manager database
conn.execute('''
Create table manager (
    ref_id VARCHAR(100) PRIMARY KEY,
    employee_id text,
    type VARCHAR(100),
    no_of_leaves INT,
    reason VARCHAR(200)
)
''')
conn.close()

# Inserting data in manager database
def insert(ref_id,employee_id,type,no_of_leaves,reason):
    conn = sqlite3.connect("./sql/manager.db")
    params = (ref_id,employee_id,type,no_of_leaves,reason)
    conn.execute( f'''
    insert into manager (ref_id,employee_id,type,no_of_leaves,reason) VALUES
    (?,?,?,?,?)
    ''',params)
    conn.commit()
    conn.close()

# Function for retrieving data using ref_id as parameter
def retrieve(ref_id):
    conn = sqlite3.connect("./sql/manager.db",check_same_thread=False)
    leave_info = conn.execute( f'''
    select employee_id,type,no_of_leaves,reason from manager where ref_id=(?)
    ''',(ref_id,))
    leave_info = leave_info.fetchone()
    print (leave_info)
    conn.commit()
    conn.close()