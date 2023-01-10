from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import GetPrimeFactorization, GetGCD, GetLDET, GetCRT
from .models import PrimeFactorization, Gcd, LDET, CRT

# Create your views here.

def home(response):
    return render(response, 'main/home.html', {})

def calc_calculator(response):
    return render(response, 'main/calc_c.html', {})

def alg_calculator(response):
    return render(response, 'main/alg_c.html', {})

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
        answer = "Enter an integer."
    return render(response, 'main/prime_fac.html', {"form":form, "answer":answer})

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
        answer = "Enter Two integers."
    return render(response, 'main/gcd.html', {"form":form, "answer":answer})

def ldet(response):
    if response.method == "POST":
        form = GetLDET(response.POST)

        if form.is_valid():
            a = form.cleaned_data["a"]
            b = form.cleaned_data["b"]
            c = form.cleaned_data["c"]
            n = LDET(a=a, b=b, c=c)
            n.save()
            answer = n.get_string_answer()
            return render(response, 'main/ldet.html', {'answer': answer, "form": form})
    else:
        form = GetLDET()
        answer = "Enter integers to calculate your values."
    return render(response, 'main/ldet.html', {'form': form, 'answer':answer})
        
def crt(response):
    if response.method == "POST":
        form = GetCRT(response.POST)

        if form.is_valid():
            a = form.cleaned_data["a"]
            b = form.cleaned_data["b"]
            m = form.cleaned_data["m"]
            eq = CRT(a=a, b=b, m=m)
            eq.save()
            answer = eq.get_string_answer()
            return render(response, 'main/crt.html', {'answer': answer, "form": form})
    else:
        #is this where i check to see if m1,m2 are coprime, and pos integers?
        form = GetCRT()
        answer = "Enter integers to calculate your values."
    return render(response, 'main/crt.html', {'form': form, 'answer':answer})