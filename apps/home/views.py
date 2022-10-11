# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from apps.home.forms import PersonForm
from django.http import JsonResponse
import json
from apps.home.models import Lga, Person, Ward
from django.views.generic import ListView

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


def person(request):
    form = PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "person.html", {"form": form})

def lgas(request):
    data = json.loads(request.body)
    lgas = Lga.objects.filter(state__id=data['user_id'])
    print(lgas)
    return JsonResponse(list(lgas.values("id", "name")), safe=False)

def wards(request):
    data = json.loads(request.body)
    wards = Ward.objects.filter(lga__id=data['user_id'])
    print(wards)
    return JsonResponse(list(wards.values("id", "name")), safe=False)




class PersonListView(ListView):
    model = Person
    context_object_name = 'people'
    template_name = 'person_list.html'




