from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def home(response):
    return render(response, 'main/base.html', {})

def calc_calculator(response):
    return render(response, 'main/alg_c.html', {})

def alg_calculator(response):
    return render(response, 'main/calc_c.html', {})

def about_us(response):
    return render(response, 'main/about_us.html', {})