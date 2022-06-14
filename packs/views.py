from django.http import HttpResponse
from django.shortcuts import render
from.models import Packs

def index(request):
    packs = Packs.objects.all()
    return render(request, 'index.html', {'packs': packs})

def new(request):
    return HttpResponse('New Packs')