import pyjokes

class joke_module:
    def __init__(self):
        self.stage = 0
    
    def exec(self,message,logger):
        joke = pyjokes.get_joke()
        logger.info(f"Sent joke < {joke} > to user {message['user']} in channel {message['channel']} with channel_type {message['channel_type']}")
        return joke

def make_obj():
    return joke_module()