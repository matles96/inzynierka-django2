from django import forms
from django.forms import ModelForm
from .models import Patient, Visit
from django.contrib.auth.models import User


class PatientHistoryForm(forms.Form):
    entry = forms.CharField(required=True)
    medicine = forms.CharField(required=True)
    dose = forms.CharField(required=True)

class PatientSearchForm(forms.Form):
    pesel = forms.CharField(required=True)

class VisitSearchForm(forms.Form):
    pesel = forms.CharField(required=False)
    date = forms.DateField(required=False)

class VisitEditForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ('patient', 'doctor', 'date_time')

class VisitAddForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ('patient', 'doctor', 'date_time')