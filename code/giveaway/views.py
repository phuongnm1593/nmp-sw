from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.urls import reverse
from datetime import datetime, timedelta

from .models import Roll, SessionKey, Candidate

import string
import random

def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str + datetime.now().strftime("%Y%m%d%H%M%S")

def index(request):
    roll = get_object_or_404(Roll, is_active=True)
    if not roll.is_on():
        return HttpResponseRedirect(reverse('giveaway:fail', kwargs={'message': "This event was ended."}))
    if "HTTP_REFERER" in request.META and request.META["HTTP_REFERER"].startswith("http://atharori.net"):
    # if True:
        session_key = SessionKey(key=get_random_alphanumeric_string(50))
        session_key.save()
        return render(request, 'giveaway/form.html', {'roll': roll,'session_key':session_key})
    
    return HttpResponseRedirect(reverse('giveaway:fail', kwargs={'message': "Join this event by clicking below link."}))    
    
    # return render(request, 'giveaway/direct.html', {'roll': roll})

def fail(request,message):
    roll = get_object_or_404(Roll, is_active=True)
   
    return render(request, 'giveaway/direct.html', {'roll': roll, 'type': 'danger', 'message':message})


def success(request,message):
    roll = get_object_or_404(Roll, is_active=True)
   
    return render(request, 'giveaway/direct.html', {'roll': roll, 'type': 'success','message':message})
        
    

def register(request, session_key):
    roll = get_object_or_404(Roll, is_active=True)
    session_key = get_object_or_404(SessionKey, key=session_key)
    if not roll.is_on():
        return HttpResponseRedirect(reverse('giveaway:fail', kwargs={'message': "This event was ended."}))
        # return HttpResponseForbidden('<h1>Roll {roll} is not available now.</h1>'.format(roll=roll))
    if not session_key.is_valid():
        return HttpResponseRedirect(reverse('giveaway:fail', kwargs={'message': "Session key is invalid or expired"}))
    
    

    try:
        candidate = Candidate(roll=roll, email=request.POST['email'].strip())
        candidate.save()

        session_key.candidate = candidate
        session_key.is_active = False
        session_key.save()
    except Exception as e:
        return HttpResponseRedirect(reverse('giveaway:fail', kwargs={'message': "Internal error."}))

        
    return HttpResponseRedirect(reverse('giveaway:success', kwargs={'message': "You can do registration many times to get bigger chance."}))