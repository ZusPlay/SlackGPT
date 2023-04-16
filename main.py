import os
from slack_bolt.adapter.socket_mode import SocketModeHandler


if __name__ == '__main__':
    from handlers import app
    socket_mode_handler = SocketModeHandler(app, os.getenv('slack_app_token'))
    socket_mode_handler.start()
