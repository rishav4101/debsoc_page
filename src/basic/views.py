from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import HttpResponse 

# Create your views here.
from django.views import generic

class Home(TemplateView):
	template_name = 'index.html'