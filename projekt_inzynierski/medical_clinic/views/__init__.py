from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .medical_views import *
from .receptionist_views import *

@login_required(login_url='/medical_clinic/accounts/login/')
def index(request):
    if request.user.groups.filter(name='doctors').exists():
        print("A")
        return redirect('medic_visits')
    elif request.user.groups.filter(name='reception').exists():
        print("A")
        return redirect('reception_home')
    elif request.user.groups.filter(name='administration').exists():
        print("A")
        return redirect('admin/')
    else:
        print("A")
        return render(request, 'medical_clinic/indexx.html', {})

