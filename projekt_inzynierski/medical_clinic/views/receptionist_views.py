from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView 
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.edit import DeleteView, FormView
from django.http import HttpResponse
from django.urls import reverse
from ..models import Visit, Patient
from ..forms import PatientSearchForm, VisitSearchForm, VisitAddForm, VisitEditForm
from django.contrib.auth.models import User

class ReceptionHomePage(PermissionRequiredMixin, TemplateView):
    permission_required = 'medical_clinic.is_reception'
    template_name = "medical_clinic/recepcja_home.html"

class AddPatient(PermissionRequiredMixin, CreateView):
    permission_required = 'medical_clinic.is_reception'
    model = Patient
    fields = '__all__'
    template_name = 'medical_clinic/reception_add_patient.html'

    def get_success_url(self):
        return reverse('reception_patient_show',args=(self.object.pk,))

class AddVisit(PermissionRequiredMixin, CreateView):
    permission_required = 'medical_clinic.is_reception'
    model = Visit
    form_class = VisitAddForm
    template_name = 'medical_clinic/reception_add_visit.html'

    def get_context_data(self, **kwargs):
        context = super(AddVisit, self).get_context_data(**kwargs)
        context['doctors'] = User.objects.filter(groups__name='doctors')
        context['patient'] = Patient.objects.filter(pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse('reception_patient_show',args=(self.object.patient.pk,))

class PatientSearchReception(PermissionRequiredMixin, ListView):
    permission_required = 'medical_clinic.is_reception'
    model = Patient
    form_class = PatientSearchForm
    context_object_name = 'patients'
    template_name = 'medical_clinic/reception_search_patient.html'
    patients = []

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            return Patient.objects.filter(pesel=form.cleaned_data['pesel'])
        return Patient.objects.all()

class VisitSearch(PermissionRequiredMixin, ListView):
    permission_required = 'medical_clinic.is_reception'
    model = Visit
    form_class = VisitSearchForm
    context_object_name = 'visits'
    template_name = 'medical_clinic/reception_search_visit.html'
    visits = []

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            form = form.cleaned_data
            print(form)
            if form['pesel'] and form['date']:
                return Visit.objects.filter(date_time__date=form['date']).filter(patient__pesel=form['pesel'])
            elif form['date']:
                return Visit.objects.filter(date_time__date=form['date'])
            elif form['pesel']:
                return Visit.objects.filter(patient__pesel=form['pesel'])
        return Visit.objects.all()

class EditPatient(PermissionRequiredMixin, UpdateView ):
    permission_required = 'medical_clinic.is_reception'
    model = Patient
    fields = '__all__'
    template_name = 'medical_clinic/reception_edit_patient.html'

    def get_success_url(self):
        return reverse('reception_patient_show',args=(self.object.pk,))

class EditVisit(PermissionRequiredMixin, UpdateView ):
    permission_required = 'medical_clinic.is_reception'
    model = Visit
    template_name = 'medical_clinic/reception_edit_visit.html'
    form_class = VisitEditForm
    visits = []

    def get_success_url(self):
        print(self.object.patient.pk)
        return reverse('reception_patient_show',args=(self.object.patient.pk,))

class DeleteVisit(PermissionRequiredMixin, DeleteView ):
    permission_required = 'medical_clinic.is_reception'
    model = Visit

    def get_success_url(self):
        return reverse('reception_patient_show',args=(self.object.patient.pk,))

class ShowPatient(PermissionRequiredMixin, DetailView):
    permission_required = 'medical_clinic.is_reception'
    template_name = "medical_clinic/reception_show_patient.html"
    model = Patient

    def get_context_data(self, **kwargs):
        context = super(ShowPatient, self).get_context_data(**kwargs)
        context['visits'] = Visit.objects.filter(patient__pk=self.kwargs['pk'])
        context['patient_info'] = Patient.objects.filter(pk=self.kwargs['pk'])[0]
        context['aa'] = 'tttr'
        return context