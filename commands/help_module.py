class help_module:
    def __init__(self):
        self.stage = 0
    
    def exec(self,message,logger,command):
        if not command:
            logger.info(f"Display help to user {message['user']} in channel {message['channel']} with channel_type {message['channel_type']}")
            return '''Help:
Use . prefix to send commands
To get more help on specific commands use help <command-name>

Commands: leave, nleaves, leavehist, help, register, joke'''
        
        ret = ""
        for help_fn in command:
            match help_fn:
                case "leave":
                    ret+="leave: Apply for a leave using this function. Follow the steps and you should be good to go!\n"
                
                case "nleaves":
                    ret+="nleaves: Tells you the number of leaves.\n"
                
                case "leavehist":
                    ret+="leavehist: Tells you all of your approved prior leaves.\n"
                
                case "help":
                    ret+="help: That's the command that you are using right now! To get help on specific topics use .help <command-name1> <command-name2> ...\n"
                
                case "register":
                    ret+="register: Use this command to register yourself. Follow the steps to complete your registration.\n"
                
                case "joke":
                    ret+="joke: Use this command to read some light-hearted CS jokes.\n"
        
        return ret


def make_obj():
    return help_module()