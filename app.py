import logging
import os
import re

from dotenv import load_dotenv
import pyjokes
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv()

SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

app = App(token=SLACK_BOT_TOKEN, name="Joke Bot")
logging.basicConfig(filename="log")
logger = logging.getLogger(__name__)

@app.message(re.compile("^joke$"))
def show_random_joke(message, say):
    channel_type = message["channel_type"]
    # if channel_type != "im":
    #     return
    
    dm_channel = message["channel"]
    user_id = message["user"]

    joke = pyjokes.get_joke()
    logger.info(f"Sent joke < {joke} > to user {user_id}")

    say(text=joke, channel=dm_channel)

@app.event("message")
def handle_message_events(message, logger):
    logger.info(f"Invalid message recieved: {message}")

def main():
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()

if __name__ == "__main__":
    main()