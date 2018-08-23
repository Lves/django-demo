# -*- coding: utf-8 -*- 

from django.http import HttpResponse
from django.shortcuts import render_to_response

def search_form(request):
    return render_to_response('search.html')

def search(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = 'You Search 是:'+request.GET['q']
    else:
        message = 'none!!!'
    return HttpResponse(message)    
