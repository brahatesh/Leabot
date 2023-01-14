import sqlite3
class nleaves:
    def __init__(self):
        stage = 0
    
        
    def exec(self,message,logger):
        reply=""
        conn = sqlite3.connect(".\sql\employee.db",check_same_thread=False)
        emp_id=message['user']
        leaves_remaining =conn.execute( f'''
        select emp_leaves from employee1 where emp_id=(?)
        ''',(emp_id,))
        leaves_remaining =leaves_remaining.fetchone()
        # return(leaves_remaining)
        reply=f"Your remaining number of leaves is {leaves_remaining[0]}"

        # logger.info(f"For User {message['user']} in channel {message['channel']} with channel_type {message['channel_type']} number of remaining leaves is {leaves_remaining[0]}" )
        conn.commit()
        conn.close()
        # print(reply)
        return reply


def make_obj():
    return nleaves()

# message={'user':"U04JMH6NV7Y"}
# mod=nleaves().exec(message,0)
