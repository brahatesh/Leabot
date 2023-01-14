import sqlite3

class nleaves:
    def __init__(self):
        self.stage = 0
    
        
    def exec(self,message,logger):
        reply=""
        conn = sqlite3.connect(".\sql\employee.db",check_same_thread=False)
        emp_id=message['user']

        leaves_remaining =conn.execute( f'''
        select emp_leaves from employee1 where emp_id=(?)
        ''',(emp_id,))
        leaves_remaining =leaves_remaining.fetchone()
        
        reply=f"Your remaining number of leaves is {leaves_remaining[0]}"
        conn.commit()
        conn.close()
        return reply


def make_obj():
    return nleaves()
