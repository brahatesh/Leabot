import re
import sys
import os

sys.path.append(os.path.abspath("./sql"))
import manager

class process_leave_module:
    def __init__(self):
        self.stage = 0
    
    def exec(self,message,logger):
        args = re.split(' ',message['text'])
        data = manager.retrieve_ref(args[1])
        if not data: 
            return "Invalid reference ID"
        match args[2]:
            case "a":