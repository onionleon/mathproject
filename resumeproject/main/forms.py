from django import forms

class GetPrimeFactorization(forms.Form):
    num = forms.IntegerField(label="Number")

class GetGCD(forms.Form):
    a = forms.IntegerField(label="First Number")
    b = forms.IntegerField(label="Second Number")