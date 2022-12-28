from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import GetPrimeFactorization, GetGCD
from .models import PrimeFactorization, Gcd 

# Create your views here.

def home(response):
    return render(response, 'main/base.html', {})

def calc_calculator(response):
    return render(response, 'main/alg_c.html', {})

def alg_calculator(response):
    return render(response, 'main/calc_c.html', {})

def about_us(response):
    return render(response, 'main/about_us.html', {})

def prime_fac(response):
    if response.method == "POST":
        form = GetPrimeFactorization(response.POST)

        if form.is_valid():
            n = form.cleaned_data["num"]
            c = PrimeFactorization(num=n)
            c.save()
            answer = c.get_string_answer()
            return render(response, 'main/prime_fac.html', {"form":form, "answer":answer})
    else:
        form = GetPrimeFactorization()
    return render(response, 'main/prime_fac.html', {"form":form})

def gcd(response):
    if response.method == "POST":
        form = GetGCD(response.POST)

        if form.is_valid():
            num1 = form.cleaned_data["a"]
            num2 = form.cleaned_data["b"]
            n = Gcd(a=num1, b=num2)
            n.save()
            answer = n.get_gcd()
            return render(response, 'main/gcd.html', {"form":form, "answer":answer})
    else: 
        form = GetGCD()
    return render(response, 'main/gcd.html', {"form":form})
    