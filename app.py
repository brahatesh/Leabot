import logging
import os
import sys
import re
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

sys.path.append(os.path.abspath("./sql"))
sys.path.append(os.path.abspath("./commands"))

import commands
import manager
import employee

load_dotenv()

SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

app = App(token=SLACK_BOT_TOKEN, name="Leabot")
logging.basicConfig(filename=".log", encoding="utf-8", level=logging.DEBUG)
logger = logging.getLogger(__name__)

if not os.path.exists('./sql/manager.db'):
    manager.make_db()
if not os.path.exists("./sql/employee.db"):
    employee.make_emp_db()

form_progress = {}


@app.event("message")
def handle_message_events(message, logger, say):
    text = message["text"].lower()
    channel = message['channel']
    if message["channel_type"] != "im":
        return
    user_id = message["user"]

    if user_id in form_progress:
        rep = form_progress[user_id].exec(text, logger, form_progress, say)
        say(text=rep, channel=message['channel'])
        return

    if text[0] != ".":
        if user_id == "U04JMH6NV7Y":
            ret = commands.pl_manager.make_obj().exec(message, logger, say)
            if ret:
                say(text=ret, channel=channel)
                return
            logger.info(f"Invalid command recieved < {message} > by {user_id}")
            ret = "Invalid command\nUse '.' as a prefix to send commands\nTo view all commands use .help"
        say(text=ret, channel=channel)
        return

    command = text[1:].lower()
    if re.match("help$", command) or re.match("help ", command):
        ret = commands.help.make_obj().exec(
            message, logger, re.split(' ', command)[1:])
        say(text=ret, channel=channel)
        return

    match command:
        case "joke":
            ret = commands.joke.make_obj().exec(message, logger)
            say(text=ret, channel=channel)

        case "leave":
            mod = commands.leave.make_obj()
            ret = mod.exec(message, logger, form_progress, say)
            form_progress[user_id] = mod
            say(text=ret, channel=channel)

        case "leavehist":
            ret = commands.leave_history.make_obj().exec(message, logger)
            say(text=ret, channel=channel)

        case "nleaves":
            ret = commands.number_leaves.make_obj().exec(message, logger)
            say(text=ret, channel=channel)

        case "register":
            mod = commands.add_employee.make_obj()
            ret = mod.exec(message, logger, form_progress,say)
            if not re.match(".*reg.*", ret):
                form_progress[user_id] = mod
            say(text=ret, channel=channel)

        case default:
            say(text="Invalid command\nUse '.' as a prefix to send commands\nTo view all commands use .help", channel=channel)


def main():
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()


if __name__ == "__main__":
    main()
