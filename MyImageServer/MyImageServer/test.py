# -*- coding: UTF-8 -*-
from django.http import HttpResponse

def test(request):
    return HttpResponse("Hello, this is test page.")