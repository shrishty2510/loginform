from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Home page')

def learn_django(request):
    return HttpResponse('Hello django')

def learn_python(request):
    return HttpResponse('Hello python')

def learn_math(request):
    a=30+50
    return HttpResponse(a)

def learn_var(request):
    return HttpResponse('<h2>How r u?</h2>')

def learn_format(request):
    a='<h3><i> never give up <i><h3>'
    return HttpResponse(f'# {a}')
