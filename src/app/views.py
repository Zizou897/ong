from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.http import JsonResponse

from core import settings
from .models import Messages
from .functions import (
    get_some_cas,
    get_all_cas
)
# Create your views here.


def home(request):
    
    get_some_cass = get_some_cas({'publish':True})
    
    template_name = "app/layouts/index.html"
    context = {
        'get_some_cas': get_some_cass
    }
    return render(request, template_name, context)


def contact(request):
    
    get_all_cass = get_all_cas({'publish':True})
    
    template_name = "app/layouts/contact.html"
    context = {
        'get_all_cas': get_all_cass
    }
    return render(request, template_name, context)


def cas(request):
    
    get_all_cass = get_all_cas({'publish':True})
    
    template_name = "app/layouts/cas.html"
    context = {
        'get_all_cas': get_all_cass
    }
    return render(request, template_name, context)


def about(request):
    
    get_all_cass = get_all_cas({'publish':True})
    
    template_name = "app/layouts/about.html"
    context = {
        'get_all_cas': get_all_cass
    }
    return render(request, template_name, context)



def verify_email(email):
    try:
        validate_email(email)
        return False
    except ValidationError:
        return True
    

@csrf_exempt
def send_post_mail(request):
    all_is_true = False
    msg = ''
    
    name = request.POST.get('name')
    message =  request.POST.get('message')
    email = request.POST.get('email')
    subject =  request.POST.get('subject')
    
    if not name or name.isspace() or not email or email.isspace() :
        msg = 'Veuillez renseigner les champs vides'
    elif verify_email(email):
        msg = 'veuillez renseigner un Mail correct'
    else:
        all_is_true, msg = True, "ce message est déjà envoyé"
        
        test_message, created = Messages.objects.get_or_create(name=name, message=message, email=email, subject=subject)
        if created:
            msg = 'Vous recevrez un mail de la part de ILCMEFV'
            
        
        else:
            test_message.save()
        
    
    data = {
        'success': all_is_true,
        'msg': msg
    }
    
    return JsonResponse(data,safe=False)