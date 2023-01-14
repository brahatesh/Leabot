import sys
import os

sys.path.append(os.path.abspath("./sql"))
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
            if not obj[4]: continue
            str+=f"{employee_fetch[0]} has taken {obj[1]} {obj[0]} leave{'s' if obj[1]>1 else ''} due to {obj[2]}\n"

        return str

def make_obj():
    return history_module_manager()
