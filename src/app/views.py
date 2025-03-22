from django.shortcuts import render

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