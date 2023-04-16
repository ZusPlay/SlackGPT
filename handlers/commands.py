import logging
from pprint import pprint
from openai import InvalidRequestError
from loader import app, gpt_chain


@app.command('/id')
def change_settings(ack, respond, command):
    ack()
    pprint({'ack': ack, 'respond': respond, 'command': command})
    respond(f'Your ID is `{command["user_id"]}`.')


@app.event('message')
def message_handler(message, say):
    pprint({'message': message, 'say': say})
    try:
        output = gpt_chain.predict(human_input=message['text'])
        say(output)
    except InvalidRequestError as error:
        logging.critical(error)
