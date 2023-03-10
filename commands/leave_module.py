import sys
import os
import uuid

import manager
import employee
sys.path.append(os.path.abspath("./sql"))


class leave_module:
    def __init__(self):
        self.stage = 0

    def exec(self, message, logger, form_progress, say):
        match self.stage:
            case 0:
                self.emp_name, self.nleaves = employee.emp_retrieve(
                    message['user'])
                self.slack_id = message['user']
                self.c_id = message['channel']

                ret = f'''You have {self.nleaves} leaves left.
What kind of leave do you want? [paid/sick]'''
                self.stage += 1
                form_progress[self.slack_id] = self
                return ret

            case 1:
                if (message not in ["paid", "sick"]):
                    ret = "Choose from paid/sick"
                    return ret

                self.leave_type = message
                ret = "How many days?"
                self.stage += 1
                form_progress[self.slack_id] = self
                return ret

            case 2:
                try:
                    nleaves_req = int(message)
                except ValueError:
                    return "Invalid number of days. Please try again."

                if (nleaves_req > self.nleaves or nleaves_req <= 0):
                    return "Invalid number of days. Please try again."
                self.nleaves = nleaves_req

                ret = "What is the reason for the leave?"
                self.stage += 1
                form_progress[self.slack_id] = self
                return ret

            case 3:
                self.id = uuid.uuid1()
                ret = f"Your request has been sent.\nReference number: {self.id}"
                man = f'''Application for leave
Name: {self.emp_name}
No of days: {self.nleaves}
Reason: {message}
Reference ID: {self.id}
Respond with {self.id} a/r/view [Refer help for details]'''

                say(text=man, channel="U04JMH6NV7Y")
                manager.insert(str(self.id), self.slack_id, self.leave_type,
                               self.nleaves, message, self.c_id, False)
                del form_progress[self.slack_id]
                return ret


def make_obj():
    return leave_module()
