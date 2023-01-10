from django import forms

class GetPrimeFactorization(forms.Form):
    num = forms.IntegerField(label="Number")

class GetGCD(forms.Form):
    a = forms.IntegerField(label="First Number")
    b = forms.IntegerField(label="Second Number")

class GetLDET(forms.Form):
    a = forms.IntegerField(label="A")
    b = forms.IntegerField(label="B")
    c = forms.IntegerField(label="C")

class GetCRT(forms.Form):
    a = forms.IntegerField(label="A")
    b = forms.IntegerField(label="B")
    m = forms.IntegerField(label="enter ur mod here")