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
    a1 = forms.IntegerField(label="A1")
    b1 = forms.IntegerField(label="B1")
    m1 = forms.IntegerField(label="Mod 1")
    a2 = forms.IntegerField(label="A2")
    b2 = forms.IntegerField(label="B2")
    m2 = forms.IntegerField(label="Mod 2")