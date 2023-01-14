import re
import sys
import os

sys.path.append(os.path.abspath("./sql"))
import manager
import employee

class process_leave_module:
    def __init__(self):
        self.stage = 0
    
    def exec(self,message,logger,say):
        args = re.split(' ',message['text'])
        data = manager.retrieve_ref(args[1])
        if not data: 
            return "Invalid reference ID"
        match args[2]:
            case "a":
                _,no_leaves,_,c_id,_ = manager.retrieve_ref(args[1])[3]
                if no_leaves > employee.emp_retrieve()
                say(text=f"Your leave with reference ID {args[1]} has been accepted", channel=c_id)
                manager.mutate(args[1], True)
                return ""
            
            case "r":
                c_id = manager.retrieve_ref(args[1])[3]
                say(text=f"Your leave with reference ID {args[1]} has been rejected", channel=c_id)
            

                