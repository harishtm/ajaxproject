from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import Context, loader, RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from datetime import datetime
from country.models import *
import json


def home(request):
    country_list = MyCountry.objects.all()
    return render(request,'test.html',locals())

def get_states(request):
    status = "Fail"
    cid = request.GET.get('cid')
    if cid:
        st_list = State.objects.filter(country__id = int(cid)).values('id','name')
        status = "Success"
    resp = {'status':status,'res':list(st_list)}
    return HttpResponse(json.dumps(resp),mimetype="application/json")
