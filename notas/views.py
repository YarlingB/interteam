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
from publicaciones.models import *
from galerias.models import *
from opiniones.models import *
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
	eventos = Agendas.objects.filter(publico=True).order_by('-inicio','-hora_inicio')[:4]
	paises = Pais.objects.all()
	contrapartes = Contraparte.objects.all()

	publicaciones = Publicacion.objects.order_by('-id')[:3]

	#galerias
	galerias = {}
	for x in Temas.objects.all():
		galeria = GaleriaImagenes.objects.filter(tematica = x).order_by('-id')[:2]
		if galeria.exists():
			galerias[x] = galeria

	#opiniones
	opiniones = Opiniones.objects.order_by('-id')

	return render(request, template, locals())

def logout_page(request):
  logout(request)
  return HttpResponseRedirect('/')

def lista_notas(request,template='blog.html'):
	notas_list = Notas.objects.all().order_by('-fecha','-id')
	hoy = datetime.date.today()
	eventos = Agendas.objects.filter(inicio__gte = hoy, publico = True).order_by('inicio')[:3]
	paises = Pais.objects.all()

	dic_temas = {}
	for tema in Temas.objects.all():
		count = Notas.objects.filter(temas = tema).count()
		dic_temas[tema] = count

	return render(request, template, locals())

def detalle_notas(request, slug, template='blog-details.html'):
	nota = get_object_or_404(Notas, slug=slug)
	nota.vistas = nota.vistas + 1
	nota.save() 
	ultimas_notas = Notas.objects.exclude(slug = slug).order_by('-fecha','-id')[:4]
	hoy = datetime.date.today()
	eventos = Agendas.objects.filter(inicio__gte = hoy, publico = True).order_by('inicio')[:3]

	dic_temas = {}
	for tema in Temas.objects.all():
		count = Notas.objects.filter(temas = tema).count()
		dic_temas[tema] = count


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

def filtro_temas(request, temas, template='blog.html'):
	notas_list = Notas.objects.filter(temas__nombre = temas).order_by('-fecha','-id')
	hoy = datetime.date.today()
	eventos = Agendas.objects.filter(inicio__gte = hoy, publico = True).order_by('inicio')[:3]

	dic_temas = {}
	for tema in Temas.objects.all():
		count = Notas.objects.filter(temas = tema).count()
		dic_temas[tema] = count

	return render(request, template, locals()) 

def publicaciones(request, template='biblioteca.html'):
	object_list = Publicacion.objects.order_by('-id')

	return render(request, template, locals())

def organizaciones(request, template='organizaciones.html'):
	object_list = Contraparte.objects.order_by('nombre')

	return render(request, template, locals())

def detalle_organizacion(request, slug, template='detalle_org.html'):
	object = get_object_or_404(Contraparte, slug=slug)

	return render(request, template, locals())