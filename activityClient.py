from random import shuffle

request_activity_list = None
elements = []

def get_vacation_element():
    element = {
        'title': 'Plan for a vacation',
        'buttons': [{
            'type' : 'web_url',
            'title' : "Check Link",
            'url' : "https://www.facebook.com/search/top?q=vacation"
        }],
        "image_url":"https://icon-library.net/images/vacation-icon-png/vacation-icon-png-13.jpg"
    }

    return element
    


def get_family_element():
    element = {
        'title': 'Connect with your family',
        'buttons': [{
            'type' : 'web_url',
            'title' : "Visit family groups",
            'url' : "https://www.facebook.com/search/top?q=family"
        }],
        "image_url":"https://icon-library.net/images/icon-for-family/icon-for-family-2.jpg"
    }

    return element
        


def get_friends_element():
    element = {
        'title': 'Meet with your friends',
        'buttons': [{
            'type' : 'web_url',
            'title' : "Check friends",
            'url' : "https://www.facebook.com/search/top?q=friends"
        }],
        "image_url":"https://www.iconspng.com/images/friends-icon.jpg"
    }

    return element

def get_activity_element():
    element = {
        'title': 'Do some activity',
        'buttons': [{
            'type' : 'web_url',
            'title' : "Check activities",
            'url' : "https://www.facebook.com/search/top?q=activities%20near%20me"
        }],
        "image_url":"https://icon-library.net/images/activities-icon/activities-icon-7.jpg"
    }

    return element
    

def get_jokes_element():

    element = {
        'title': 'Laugh out loud',
        'buttons' : [{
            'type': 'web_url',
            'title': "Check group",
            'url': "https://www.facebook.com/LaughsQuotesJokesFunnies/"
        }],
        "image_url": "https://icon-library.net/images/funny-icon-png/funny-icon-png-9.jpg"
    }

    return element

def get_music_element():

    element = {
        'title': 'Unwind to Music',
        'buttons' : [{
            'type': 'web_url',
            'title': "Listen",
            'url': "https://open.spotify.com/"
        }],
        "image_url": "http://www.myiconfinder.com/uploads/iconsets/256-256-bc0fd466e19a29c9e96f2471dd41eb83-spotify.png"
    }

    return element

def get_movie_element():
        element = {
            'title': 'Netflix time!',
            'buttons' : [{
                'type': 'web_url',
                'title': "Watch",
                'url': "https://www.facebook.com/netflixus/?brand_redir=1781104715514072"
            }],
            "image_url": "https://i.pinimg.com/originals/8c/51/0e/8c510ee7de078ac4eaafdb9d15a810dd.png"
        }
        # },{
        #     'title': 'This is a Facbook Movie Element',
        #     'buttons' : [{
        #         'type': 'web_url',
        #         'title': "Read More",
        #         'url': "https://www.facebook.com/facebookwatch"
        #     }],
        #     "image_url": ""
        # }]
        return element

def get_workout_element():
        element = {
            'title': 'Do some workout',
            'buttons' : [{
                'type': 'web_url',
                'title': "See group",
                'url': "https://www.facebook.com/MuscleandFitnessMag"
            }],
            "image_url": "https://icon-library.net/images/workout-icon/workout-icon-6.jpg"
        }

        return element

def get_restaurant_element():
        element = {
            'title': 'Eat out today',
            'buttons' : [{
                'type': 'web_url',
                'title': "Nearby Restaurants",
                'url': "https://www.facebook.com/search/top?q=restaurants%20near%20me"
            }],
            "image_url": "https://iconsplace.com/wp-content/uploads/_icons/000000/256/png/restaurant-icon-256.png"
        }

        return element

def get_doctor_element():
    element = {
        'title' : 'Take medical care',
        'buttons' : [{
            'type' : 'web_url',
            'title' : "Click",
            'url' : "https://www.facebook.com/search/top?q=medical%20emergency"
        }],
        "image_url":"https://icon-library.net/images/doctor-icon/doctor-icon-15.jpg"
    }
    return element

activity_dict = {'music' : get_music_element() ,
                 'friends': get_friends_element() ,
                 'movie': get_movie_element() ,
                 'workout': get_workout_element() ,
                #  'partner': get_partner_element() ,
                 'doctor': get_doctor_element() ,
                 'activity': get_activity_element() ,
                 'vacation': get_vacation_element() ,
                 'restaurant': get_restaurant_element() ,
                 'jokes': get_jokes_element() ,
                 'family': get_family_element() ,
                #  'share': get_share_element()
                 }
negative_message_list = ["Cheer Up! The world is wonderful place, you can do so much ","It's okay! Go do some fun things outside", "Dont worry, life will become better"]
positive_message_list = ["That's Great!","Sounds awesome!","Enjoy your day","Remarkable"]
neutral_message_list = ["Try some fun things", "Want to do some activities", "Go out and enjoy"]


def get_element(activityList = None):
    request_activity_list = activityList
    elements = []
    if 'doctor' in activityList:
        elements.append(get_doctor_element())
        activityList.remove('doctor')
    if 'share' in activityList:
        activityList.remove('share')
    if 'partner' in activityList:
        activityList.remove('partner')
    shuffle(activityList)
    if activityList is not None:
        for activity in activityList:
            # print(activity)
            elements.append(activity_dict[activity])
            if len(elements) > 5:
                return elements
    else:
        elements = []
    return elements
def get_emotion_response(emot = None):
   
    message_text = ""
    emot = str(emot)
    print(emot)
    if emot == 'TooNegative':
        shuffle(negative_message_list)
        message_text = negative_message_list[0]
    elif emot == 'Negative':
        shuffle(negative_message_list)
        message_text = negative_message_list[0]
    elif emot == 'Neutral':
        shuffle(neutral_message_list)
        message_text = neutral_message_list[0]
    elif emot == 'Positive':
        shuffle(positive_message_list)
        message_text = positive_message_list[0]
    elif emot == 'TooPositive':
        shuffle(positive_message_list)
        message_text = positive_message_list[0]
    else:
        # shuffle(positive_message_list)
        message_text = ""
    return message_text
# print(get_element(['music','friends','movie','partner','family']))
# def get_music_temp():

# print(get_emotion_response('Negative'))


