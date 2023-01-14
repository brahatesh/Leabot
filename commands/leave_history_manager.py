import sys
import os
sys.path.append(os.path.abspath("./sql"))
# from manager_side.retrieve import retrieve as history_ret
import manager
import employee

class history_module_manager:
     def __init__(self):
        self.stage = 0

     def exec(self,message,logger,ref_id):
        ## here we are retrieving all leave history of an employee for the manager
        emp_det = manager.retrieve_ref(ref_id)
        employee_fetch = employee.emp_retrieve(emp_det[0])
        leave_hist = manager.retrieve(emp_det[0])
        str = ""
        for obj in leave_hist:
            # print(obj)
            str+=f"{employee_fetch[0]} has taken {obj[1]} {obj[0]} leave{'s' if obj[1]>1 else ''} due to {obj[2]}\n"

        # logger.info(f"Sent string < {str} > to user {message['user']} in channel {message['channel']} with channel_type {message['channel_type']}")
        print(str)
        return str
# message = {'user':'U04JMH6NV7Y'}
# mod = history_module().exec(message,0)
def make_obj():
    return history_module_manager()
