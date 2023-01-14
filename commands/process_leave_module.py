import re
import sys
import os

sys.path.append(os.path.abspath("./sql"))
import manager
import employee
import leave_history_manager

class process_leave_module:
    def __init__(self):
        self.stage = 0
    
    def exec(self,message,logger,say):
        args = re.split(' ',message['text'])
        if len(args[0])!=36:
            return ""
        data = manager.retrieve_ref(args[0])
        if not data: 
            return "Invalid reference ID"
        match args[1]:
            case "a":
                emp_id,_,no_leaves,_,c_id,_ = manager.retrieve_ref(args[1])[3]
                if no_leaves > employee.emp_retrieve(emp_id)[1]:
                    say(text=f"Your leave with reference ID {args[0]} has been rejected due to error\n<no_of_days_applied> > <no_of_days_available>", channel=c_id)
                    manager.delete_ref(args[0])
                    return f"{args[0]} rejected because <no_of_days_applied> > <no_of_days_available"
                say(text=f"Your leave with reference ID {args[0]} has been accepted", channel=c_id)
                manager.mutate(args[0], True)
                return f"{args[0]} accepted"
            
            case "r":
                c_id = manager.retrieve_ref(args[0])[3]
                say(text=f"Your leave with reference ID {args[0]} has been rejected", channel=c_id)
                manager.delete_ref(args[0])
                return f"{args[0]} rejected"

            case "view":
                return leave_history_manager.make_obj().exec(_,logger,args[0])
            
            case default:
                return f"Invalid argument provided for reference ID {args[0]}"

def make_obj():
    return process_leave_module()