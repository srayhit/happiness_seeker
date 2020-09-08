import os, sys
# from utils import wit_response

import utils as ut

from flask import Flask, request
from pymessenger import Bot
import activityClient as ac

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
                        print("No message")
                        messaging_text = None
                    
                    #ECHO
                    print(messaging_text)   
                    # response = messaging_text
                    if messaging_text is not None:

                        greetings = ut.is_greetings(messaging_text)
                        # print(greetings)
                        if greetings:
                            response = ut.handle_greetings()
                            print(response)
                            bot.send_text_message(sender_id,response)
                        else:
                            emot , emotconf = ut.get_emotion(messaging_text)
                            sent , sentconf = ut.get_sentiment(messaging_text)
                            cont, contconf = ut.get_context(messaging_text)
                            # print(emot,sent,cont)


                            util_resp = ut.handle_response(emot,sent,emotconf,sentconf)
                            action_resp = ut.generate_action(util_resp,cont,contconf)
                            act_list = action_resp
                            share_var = False
                            partner_var = False
                            if 'share' in act_list:
                                share_var = True
                            if 'partner' in act_list:
                                partner_var = True
                            

                            elements = ac.get_element(action_resp)
                            resp_emot = ac.get_emotion_response(util_resp)
                            default_text = "These are my suggestions"
                            response = resp_emot + "\n" + default_text
                            

                            bot.send_text_message(sender_id,response)
                            if elements :
                                bot.send_generic_message(sender_id,elements)

                            if share_var:
                                # print('here')
                                bot.send_text_message(sender_id,'You can also share your achievement on you wall!')
                            if partner_var:
                                # print('here')
                                bot.send_text_message(sender_id,'You can also call your partner')

                    
                    

                    # bot.send_text_message(sender_id,response)


    return "ok", 200

def log(message):
    print(message) 
    sys.stdout.flush()

if __name__ == "__main__":
    app.run(debug = True, port = 80)
