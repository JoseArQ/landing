from django import forms

class SearchForm(forms.Form):
    city = forms.CharField()
    date_arrival = forms.DateField()
    date_departure = forms.DateField()
    guest = forms.IntegerField()
    