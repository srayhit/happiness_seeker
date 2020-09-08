from wit import Wit
from random import shuffle

server_access_token = "RHQEAJXGLYODSL3CYVLJXWC7CI7FMVBF"

client = Wit(access_token = server_access_token)


emotions_list = ['help', 'Sad', 'celebrate', 'happy', 'chill', 'bored']
context_list = ['job', 'Family', 'exam', 'activity']
pos_actions_list = ['music', 'friends', 'share', 'vacation', 'family', 'restaurant','movies','workout']
neg_actions_list = ['jokes', 'music', 'friends', 'vacation', 'family', 'restaurant','movies','workout','partner','doctor']
neu_actions_list = ['music', 'friends','movies','workout','partner','doctor']

sent_thresh = 0.5
emot_thresh = 0.6

greeting_list = ['Hi There!', 'Hello', 'Nice of you to interact','Greeetings!']

def first_value(obj, key):
    if key not in obj:
        return None
    val = obj[key][0]['value']
    if not val:
        return None
    return val


# def handle_message(response):
    # traits = response['traits']
    # emotion = first_value(traits, 'get_emotion')
    # greetings = first_value(traits, 'wit$greetings')
    # emotion = first_value(response['entities'], 'category:category')
    # sentiment = first_value(traits, 'wit$sentiment')
    ## Check for different entities
    # isemotion = search_object(wit_response['entities'],'get_emotion:get_emotion')
    # isaction = search_object(wit_response['entities'],'get_action:get_action')
    # iscontext = search_object(wit_response['entities'],'get_context:get_context')
        
    # emotion = first_value(wit_response['entities'],'get_emotion:get_emotion') if isemotion else None
    # action = first_value(wit_response['entities'],'get_action:get_action') if isaction else None
    # context = first_value(wit_response['entities'],'get_context:get_context') if iscontext else None

    # print(response)
    # if get_joke:
    #     return select_joke(category)
    # elif sentiment:
    #     return 'Glad you liked it.' if sentiment == 'positive' else 'Hmm.'
    # elif greetings:
    #     return 'Hey this is joke bot :)'
    # else:
    #     return 'I can tell jokes! Say "tell me a joke about tech"!'



# def wit_response(message_text):
#     resp = client.message(message_text)

#     entity = None
#     entity_name = None
#     value = None
#     trait = None

#     try:
#         entity = list(resp['entities'])[0]
#         entity_name = resp['entities'][entity][0]["name"]
#         value = resp['entities'][entity][0]['body']
#     except:
#         pass
#     return (resp)



# print(wit_response("I passed the exam, Hoorah!"))
def search_object(object_list = [], value=None):
    return True if value in object_list else False
    

def first_confidence(obj, key):
    if key not in obj:
        return None
    val = obj[key][0]['confidence']
    if not val:
        return None
    return val


def get_message(message_text = None):
    wit_response = client.message(message_text)
    for trait in wit_response['traits']:
        if trait == 'wit$greetings':
            confidence = wit_response['traits'][trait][0]['confidence']
            greetings = True if float(confidence) > 0.85 else False



def is_greetings(message_text = None):
    greetings = False
    if message_text is not None:
        wit_response = client.message(message_text)
    else:
        return None
    for trait in wit_response['traits']:
        if trait == 'wit$greetings':
            confidence = wit_response['traits'][trait][0]['confidence']
            greetings = True if float(confidence) > 0.85 else False

    return greetings
# print(is_greetings(""))
def get_emotion(message_text = None):
    if message_text is not None:
        wit_response = client.message(message_text)
    else:
        return (None,None)
    isemotion = search_object(wit_response['entities'],'get_emotion:get_emotion')
    emotion = first_value(wit_response['entities'],'get_emotion:get_emotion') if isemotion else None
    emotion_conf = first_confidence(wit_response['entities'],'get_emotion:get_emotion') if isemotion else None
    return (emotion,emotion_conf)


def get_context(message_text = None):
    if message_text is not None:
        wit_response = client.message(message_text)
    else:
        return (None,None)
    # print(wit_response)
    iscontext = search_object(wit_response['entities'],'get_context:context')
    context = first_value(wit_response['entities'],'get_context:context') if iscontext else None
    context_conf = first_confidence(wit_response['entities'],'get_context:context') if iscontext else None
    return (context,context_conf)

def get_sentiment(message_text = None):
    if message_text is not None:
        wit_response = client.message(message_text)
    else:
        return (None,None)
    issentiment = search_object(wit_response['traits'],'wit$sentiment')
    sentiment = first_value(wit_response['traits'],'wit$sentiment') if issentiment else None
    sentiment_conf = first_confidence(wit_response['traits'],'wit$sentiment') if issentiment else None
    return (sentiment,sentiment_conf)


def handle_greetings():
    shuffle(greeting_list)
    greeting_message =  greeting_list[0] +' I am a bot, tell me how you\'re feeling?'
    return str(greeting_message)

# print(handle_greetings())

def generate_action(responseType = None, context = None, cont_conf = 0):
    cont_conf = float(cont_conf) if cont_conf is not None else 0
    action_list = []
    if responseType == 'TooNegative':
        if context == 'medical':
            action_list = ['doctor','family','partner']
        elif context == 'Family':
            action_list = ['family','partner','friends','music','movie']
        elif context == 'exam' or context == 'Job':
            action_list = ['music','friends','movie','partner','family']
        elif context == 'activity':
            action_list = ['activity','movie','music','friends']
        else:
            action_list = ['partner','family','music','friends','workout']

    elif responseType == 'Negative':
        if context == 'medical':
            action_list = ['doctor','family','partner']
        elif context == 'Family':
            action_list = ['family','partner','friends','music','movie']
        elif context == 'exam' or context == 'Job':
            action_list = ['music','friends','movie','partner','family']
        elif context == 'activity':
            action_list = ['activity','movie','music','friends']
        else:
            action_list = ['partner','family','music','friends','workout']
    elif responseType == 'Neutral':
        if context == 'medical':
            action_list = ['doctor','family','partner']
        elif context == 'Family':
            action_list = ['family','partner','friends','activity']
        elif context == 'exam' or context == 'Job':
            action_list = ['share', 'friends','movie','partner','family']
        elif context == 'activity':
            action_list = ['restaurant','activity','movie','music','friends']
        else:
            action_list = ['activity']
    elif responseType == 'Positive':
        if context == 'medical':
            action_list = ['doctor','family','partner','share','vacation','workout']
        elif context == 'Family':
            action_list = ['family','partner','friends','music','movie','restaurant','activity']
        elif context == 'exam' or context == 'Job':
            action_list = ['share', 'restaurant', 'music','friends','movie','partner','family']
        elif context == 'activity':
            action_list = ['restaurant','activity','movie','music','friends']
        else:
            action_list = ['share', 'restaurant', 'friends','activity']
    elif responseType == 'TooPositive':
        if context == 'medical':
            action_list = ['doctor','family','partner','share','vacation','workout']
        elif context == 'Family':
            action_list = ['family','partner','friends','music','movie','restaurant','activity']
        elif context == 'exam' or context == 'Job':
            action_list = ['share', 'restaurant', 'music','friends','movie','partner','family']
        elif context == 'activity':
            action_list = ['restaurant','activity','movie','music','friends']
        else:
            action_list = ['share', 'movie', 'friends', 'partner','activity']
    else:
        action_list = []
    return action_list


def handle_response(emotion=None,sentiment=None,emo_conf = 0,sent_conf=0):
    emo_conf = float(emo_conf) if emo_conf is not None else 0
    sent_conf = float(sent_conf) if sent_conf is not None else 0
    if emotion in emotions_list and (emo_conf >= emot_thresh):
        if emotion == 'Sad' or emotion == 'help':
            if sentiment == 'negative' and (sent_conf >= sent_thresh):
                return 'TooNegative'
            elif (sentiment == 'positive' or sentiment == 'neutral') and (sent_conf >= sent_thresh):
                return 'Negative'
            elif (sentiment == None):
                return 'Negative'
            else:
                return 'Unsure'

        if emotion == 'happy' or emotion == 'celebrate':
            if (sentiment == 'positive' or sentiment == 'neutral') and (sent_conf >= sent_thresh):
                return 'TooPositive'
            elif sentiment == 'negative' and (sent_conf >= sent_thresh):
                return 'Positive'
            elif (sentiment == None):
                return 'Positive'
            else:
                return 'Unsure'
        if emotion == 'chill' or emotion == 'bored':
            if (sentiment == 'neutral') and (sent_conf > sent_thresh):
                return 'Neutral'
            elif sentiment == 'positive' and (sent_conf > sent_thresh):
                return 'Positive'
            elif (sentiment == 'negative') and (sent_conf > sent_thresh):
                return 'Negative'
            elif (sentiment == None):
                return 'Neutral'
            else:
                return 'Unsure'

    else:
        if (sentiment == 'neutral') and (sent_conf > sent_thresh):
                return 'Neutral'
        elif sentiment == 'positive' and (sent_conf > sent_thresh):
            return 'Positive'
        elif (sentiment == 'negative') and (sent_conf > sent_thresh):
            return 'Negative'
        elif (sentiment == None):
            return 'Neutral'
        else:
            return 'Unsure'


# print(handle_response(emot,sent,emotconf, sentconf))

# mess = "I dont want to get up"
# print(client.message(mess))
# print(get_emotion(mess))
# print(get_context(mess))
# print(get_sentiment(mess))

# emot , emotconf = get_emotion(mess)
# sent , sentconf = get_sentiment(mess)
# cont, contconf = get_context(mess)

# respType = handle_response(emot,sent,emotconf, sentconf)
# print(respType)
# print(generate_action(respType,cont,contconf))

# print(handle_greetings())

# client.interactive(handle_message=handle_message)