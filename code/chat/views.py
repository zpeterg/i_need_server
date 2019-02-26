from django.http import HttpResponse
from respond.main import Respond
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
client = MongoClient('198.168.99.100', 27017)
db = client.sessions
sessions = client.sessions

# Create your views here.


@csrf_exempt
def index(request):
    subject = ()
    user_id = request.POST.get('user_id')
    phrase = request.POST.get('phrase')
    session = sessions.find_one({'user_id': user_id})
    print('REQUEST:::', user_id, phrase, 'SESSION:::', session)
    # If session exists for user, retrieve and delete it
    if session:
        subject = session['subject']
        sessions.delete_many({'user_id': user_id})
    respond = Respond()
    send_phrase = respond.get_response(phrase, subject)
    # Create session for user
    if send_phrase['subject']:
        reply = sessions.insert_one({
            'user_id': user_id,
            'subject': subject,
        })
        print('DB REPLY:::', reply)
    return HttpResponse(f"Response to 'food' is: {send_phrase}")
