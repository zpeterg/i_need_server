from django.http import HttpResponse
from .respond.main import Respond

# Create your views here.


def index(request):
    print('REQUEST:::', request)
    subject = ()
    respond = Respond()
    send_phrase = respond.get_response('food', subject)
    return HttpResponse(f"Response to 'food' is: {send_phrase}")
