from django.shortcuts import render
from django.http import HttpResponse
from .services import passwd_create


def index(request):
    return render(request, 'index.html')

def passwd_gen(request):
    passwd = passwd_create.Passwd()
    passwd_created = passwd.create()
    return HttpResponse(f'Password created {passwd_created}')