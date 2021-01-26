from django.views.generic.base import TemplateView

class MedicHomePage(TemplateView):
    template_name = "medical_clinic/medic_home.html"