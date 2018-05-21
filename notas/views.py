# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from .models import *
from agendas.models import *
from contrapartes.models import *
from .forms import *
# from django.contrib.contenttypes.generic import generic_inlineformset_factory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# import thread
import datetime
import operator
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.sites.models import Site


def index(request,template='index.html'):

    notas = Notas.objects.all().order_by('-fecha','-id')[:6]
    notas2 = Notas.objects.all().order_by('-fecha','-id')[1:9]
    evento = Agendas.objects.filter(publico=True).order_by('-inicio')[:4]
    paises = Pais.objects.all()
    contrapartes = Contraparte.objects.all()

    return render(request, template, locals())

def logout_page(request):
  logout(request)
  return HttpResponseRedirect('/')

def lista_notas(request,template='index.html'):
    notas_list = Notas.objects.all().order_by('-fecha','-id')
    paises = Pais.objects.all()

    paginator = Paginator(notas_list, 4)

    page = request.GET.get('page')
    try:
        notas = paginator.page(page)
    except PageNotAnInteger:
        notas = paginator.page(1)
    except EmptyPage:
        notas = paginator.page(paginator.num_pages)

    return render(request, template, locals())

def detalle_notas(request, slug, template='blog-details.html'):
    nota = get_object_or_404(Notas, slug=slug)
    ultimas_notas = Notas.objects.exclude(slug = slug).order_by('-fecha','-id')[:4]

    if request.method == 'POST':
        form = ComentarioForm(request.POST)

        if form.is_valid():
            form_uncommited = form.save(commit=False)
            form_uncommited.user = request.user
            form_uncommited.nota = nota
            form_uncommited.save()

        return HttpResponseRedirect('/notas/%d/#cmt%d' % (nota.id,form.instance.id) )

    else:
        form = ComentarioForm()

    return render(request, template, locals()) 