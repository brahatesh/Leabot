import sys
import os

sys.path.append(os.path.abspath("./sql"))
import employee

class insert_module:
    def __init__(self):
        self.stage = 0

    def exec(self, message, logger, form_progress, say):
        match self.stage:
            case 0:
                self.user_id = message['user']
                emp_inf = employee.emp_retrieve(self.user_id)
                if emp_inf:
                    ret = "You are already registered in database"
                    return ret

                ret = "Enter your full name"
                self.stage += 1
                form_progress[self.user_id] = self
                return ret

            case 1:
                employee.emp_insert(self.user_id, message, 18)
                ret = "Welcome to the organization"
                del form_progress[self.user_id]
                return ret


def make_obj():
    return insert_module()
