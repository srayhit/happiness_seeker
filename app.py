import os, sys

from flask import Flask, request
from pymessenger import Bot

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAQN1Rw6PQYBAIdmlD8O9AmfqMe5Hwn32U46m5wlyZBKBiiKciMDSZArvsIxf8zyiZA62voGgKZADiutWvO76ZAnMfg31G11BQRZBDZCotTrL6CwZAH207Aagf3ERPoYQgdcSCGdoWAgftP4hcMFNrcf0okvFLnm361qgjfyL4x3VAZDZD"
bot = Bot(PAGE_ACCESS_TOKEN)

@app.route('/',methods=['GET'])
def verify():
    #webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello" :
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200

@app.route('/', methods=['POST'])

def webhook():
    data = request.get_json()
    log(data)

    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:

                # ID's
                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']

                if messaging_event.get('message'):
                    if 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['text']
                    else:
                        messaging_text = 'no text'
                    
                    #ECHO
                    response = messaging_text

                    bot.send_text_message(sender_id,response)


    return "ok", 200

def log(message):
    print(message) 
    sys.stdout.flush()

if __name__ == "__main__":
    app.run(debug = True, port = 80)
