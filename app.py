import logging
import os
import sys
import re

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

sys.path.append(os.path.abspath("./sql"))
sys.path.append(os.path.abspath("./commands"))
from employee.employee_update import update as employee_upd
import commands

load_dotenv()

SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

app = App(token=SLACK_BOT_TOKEN, name="Joke Bot")
logging.basicConfig(filename=".log", encoding="utf-8", level=logging.DEBUG)
logger = logging.getLogger(__name__)

form_progress = {}

@app.event("message")
def handle_message_events(message, logger, say):
    text = message["text"]
    channel = message['channel']
    if message["channel_type"] != "im":
        return
    user_id = message["user"]

    if(user_id in form_progress):
        rep = form_progress[user_id].exec(message,logger)
        say(text=rep, channel=message['channel'])
        return

    if(text[0]!="."): 
        logger.info(f"Invalid command recieved < {message} > by {user_id}")
        say(text="Invalid command", channel=message["channel"])
        return

    command = text[1:].lower()
    match command:
        case "joke":
            # joke = pyjokes.get_joke()
            ret = commands.joke.make_obj().exec(message,logger)
            # logger.info(f"Sent joke < {ret} > to user {user_id} in channel {dm_channel} with channel_type {channel_type}")
            say(text=ret, channel=channel)
        
        case "update":
            employee_upd(user_id,4)

        case default:
            say(text="Invalid command", channel=channel)


def main():
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()

if __name__ == "__main__":
    main()