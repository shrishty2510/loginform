from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_dj(request):
    return HttpResponse('Hello django server')

def learn_m(request):
    a=30+3000
    return HttpResponse(a)
# Create your views here.
