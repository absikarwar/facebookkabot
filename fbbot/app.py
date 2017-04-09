import os,sys


from flask import Flask, request
from pymessenger import Bot

app = Flask(__name__)

bot = Bot("EAAEH6r7KoOsBAIVVa9ZCQ1ZC3uZBBIuXDz9VqrDaSkdOZBsbssxnDYUmK4wiXtc0GGljLOdKme5UYe5tCiBE3jZAr1FiZBGllgtjwFTZB6prUHDZBgXpqS2IQLi0xlHi9lwIhm9bNX25lZCfDokykhZB4nl4bOXQRBT8IS8fhsZC33gkwZDZD")


@app.route('/', methods=['GET'])
def verify():

    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == 'hello':
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200

@app.route('/' , methods= ['POST'])
def post_req():

    data = request.get_json()

    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:

                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']

                if messaging_event.get('message'):
                    if 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['text']
                    else:
                        messaging_text = 'no text'

                    response = messaging_text
                    bot.send_text_message(sender_id, response)

    return 'yes',200



if __name__ == '__main__':
    app.run(debug=True)