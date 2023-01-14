import sys
import os

sys.path.append(os.path.abspath("./sql"))
import manager

class history_module:
     def __init__(self):
        self.stage = 0

     def exec(self,message,logger):
        ## here we are retrieving all leave history of a employee
        leave_hist = manager.retrieve(message['user'])
        str = ""

        for obj in leave_hist:
            if not obj[4]: continue
            str+=f"You have taken {obj[1]} {obj[0]} leave{'s' if obj[1]>1 else ''} due to {obj[2]}\n"

        if not str: str = "You have not taken any leaves"
        logger.info(f"Sent string < {str} > to user {message['user']} in channel {message['channel']} with channel_type {message['channel_type']}")
        return str

def make_obj():
    return history_module()




