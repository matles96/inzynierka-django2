from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.edit import DeleteView, FormView
from django.http import HttpResponse
from ..models import Visit, PatientHistory, Patient
from datetime import date
from ..forms import PatientHistoryForm, PatientSearchForm

    
class Visits(PermissionRequiredMixin, ListView):
    permission_required = 'medical_clinic.is_doctor'
    template_name = "medical_clinic/list_visits.html"
    context_object_name = 'visits'

    def get_queryset(self):
        active_user = self.request.user.pk
        queryset = Visit.objects.filter(doctor__pk=active_user).filter(date_time__date=date.today())
        return queryset

class PatientDetail(PermissionRequiredMixin, FormView, DetailView):
    permission_required = 'medical_clinic.is_doctor'
    form_class = PatientHistoryForm
    template_name = "medical_clinic/patient_history.html"
    success_url = "patient_history"
    model = Patient

    def form_valid(self, form):
        form_data = form.cleaned_data
        discount = PatientHistory(
            patient=Patient.objects.get(pk=self.kwargs['pk']),
            entry=form_data['entry'],
            medicine=form_data['medicine'],
            dose=form_data['dose'],
        )
        discount.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PatientDetail, self).get_context_data(**kwargs)
        context['history'] = PatientHistory.objects.filter(patient__pk=self.kwargs['pk'])
        context['patient_info'] = Patient.objects.filter(pk=self.kwargs['pk'])[0]
        context['aa'] = 'tttr'
        return context

class PatientSearchMedic(PermissionRequiredMixin, ListView):
    permission_required = 'medical_clinic.is_doctor'
    model = Patient
    form_class = PatientSearchForm
    context_object_name = 'patients'
    template_name = 'medical_clinic/list_patients.html'
    patients = []


    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            return Patient.objects.filter(pesel=form.cleaned_data['pesel'])
        return Patient.objects.all()

