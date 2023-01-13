import logging
import os
import sys
import re

from dotenv import load_dotenv
import pyjokes
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

sys.path.append(os.path.abspath("./sql"))
from employee.employee_update import update as employee_upd

load_dotenv()

SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

app = App(token=SLACK_BOT_TOKEN, name="Joke Bot")
logging.basicConfig(filename=".log", encoding="utf-8", level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.message(re.compile(f"^[h|H][i|I]$"))
def show_random_joke(message, say):
    channel_type = message["channel_type"]
    if channel_type != "im":
        return
    
    dm_channel = message["channel"]
    user_id = message["user"]

    joke = pyjokes.get_joke()
    logger.info(f"Sent joke < {joke} > to user {user_id} in channel {dm_channel} with channel_type {channel_type}")

    employee_upd(user_id,4)

    say(text=joke, channel=dm_channel)

@app.event("message")
def handle_message_events(message, logger, say):
    logger.info(f"Invalid message recieved: {message}")
    say(text="Invalid command", channel=message["channel"])

def main():
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()

if __name__ == "__main__":
    main()