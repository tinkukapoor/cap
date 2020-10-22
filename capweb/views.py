#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def home1(view):
	return render_to_response('home.html')

def home(request):
	return render_to_response('Index.html')


def service(request):
	return render_to_response('service.html')


def service2(request):
	return render_to_response('service2.html')

def training(request):
	return render_to_response('training.html')


def contact(request):
	return render_to_response('contact.html')

def aboutus(view):
	return render_to_response('aboutus.html')


