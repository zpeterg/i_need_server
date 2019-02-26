from django.http import HttpResponse
from respond.main import Respond
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


@csrf_exempt
def index(request):
    print('REQUEST:::', request.POST.get('user_id'), request.POST.get('phrase'))
    phrase = request.POST.get('user_id')
    phrase = request.POST.get('phrase')
    subject = ()
    respond = Respond()
    send_phrase = respond.get_response(phrase, subject)
    return HttpResponse(f"Response to 'food' is: {send_phrase}")
