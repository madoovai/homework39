from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.template.loader import render_to_string


def home(request):
    home1 = render_to_string("home.html")
    return HttpResponse(content=home1)


def bio(request):
    bio1 = render_to_string("bio.html")
    return HttpResponse(content=bio1)


def education(request):
    edu1 = render_to_string("edu.html")
    return HttpResponse(content=edu1)


def career(request):
    work = render_to_string("work.html")
    return HttpResponse(content=work)