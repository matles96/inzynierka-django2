from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .medical_views import *
from .receptionist_views import *

@login_required(login_url='/medical_clinic/accounts/login/')
def index(request):
    if request.user.groups.filter(name='medic').exists():
        print("A")
        return redirect('medic_home')
    elif request.user.groups.filter(name='recepcja').exists():
        print("A")
        return redirect('recepcja_home')
    elif request.user.groups.filter(name='administrator').exists():
        print("A")
        return redirect('/admin/')
    else:
        print("A")
        return render(request, 'medical_clinic/indexx.html', {})

