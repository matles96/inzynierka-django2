from django.urls import path
from django.conf.urls import include, url
from . import views
from .views import ReceptionHomePage, PatientSearchMedic, Visits, PatientDetail
from .views import PatientSearchReception, VisitSearch, AddPatient, ShowPatient, AddVisit, EditPatient, EditVisit, DeleteVisit
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('medic/patient_search', PatientSearchMedic.as_view(), name='patient_search'),
    path('medic/visits', Visits.as_view(), name='medic_visits'),
    path('<int:pk>/medic/patient_history', PatientDetail.as_view(), name='patient_history'),
    path('recepcja/home', ReceptionHomePage.as_view(), name='reception_home'),
    path('<int:pk>/recepcja/patient/show', ShowPatient.as_view(), name='reception_patient_show'),
    path('recepcja/patient/search', PatientSearchReception.as_view(), name='reception_patient_search'),
    path('recepcja/visit/search', VisitSearch.as_view(), name='reception_visit_search'),
    path('recepcja/patient/add', AddPatient.as_view(), name='reception_patient_add'),
    path('<int:pk>/recepcja/visit/add', AddVisit.as_view(), name='reception_visit_add'),
    path('<int:pk>/recepcja/patient/edit', EditPatient.as_view(), name='reception_patient_edit'),
    path('<int:pk>/recepcja/visit/edit', EditVisit.as_view(), name='reception_visit_edit'),
    path('<int:pk>/recepcja/visit/delete', DeleteVisit.as_view(), name='reception_visit_delete'),
]