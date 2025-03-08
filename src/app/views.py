from django.shortcuts import render

from .functions import (
    get_some_cas
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
    
    get_some_cass = get_some_cas({'publish':True})
    
    template_name = "app/layouts/contact.html"
    context = {
        'get_some_cas': get_some_cass
    }
    return render(request, template_name, context)