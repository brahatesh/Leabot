class help_module:
    def __init__(self):
        stage = 0
    
    def exec(self,message,logger,command):
        # if not command:
        logger.info(f"Display help to user {message['user']} in channel {message['channel']} with channel_type {message['channel_type']}")
        return '''Help:
            Use . prefix to send commands
            To get more help on specific commands use help <command-name>
            
            List of commands:
            joke: Tell a joke
            leave: Apply for a leave
            nleaves: Gives the number of pending leaves
            leavehist: Gives the leave history
            help: Prints this help'''
        # for help_fn in command:

def make_obj():
    return help_module