
from django.http import HttpResponse


def home(request):
    return HttpResponse("this is a home page")

def first(request):
    return HttpResponse("first page")
