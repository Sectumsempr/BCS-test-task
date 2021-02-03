from django import forms
import datetime


class DateForm(forms.Form):
    date = forms.DateField(initial=datetime.date.today)
