from django.shortcuts import render
from firstapp.models import *

# Create your views here.

def home(request):
    return render(request, 'folders/index.html')

def motos(request):
    if request.method == 'POST':
        motobd=Motos(m_marca=request.POST["m_marca"],
                     m_modelo= request.POST["m_modelo"], 
                     m_year=request.POST["m_year"],
                     m_est=request.POST["m_est"]
                     )
        motobd.save()
        return render(request, 'folders/fmotos.html')
    return render(request,'folders/fmotos.html')

def autos(request):
    if request.method == 'POST':
        autobd=Autos(a_marca=request.POST["a_marca"],
                     a_modelo= request.POST["a_modelo"], 
                     a_year=request.POST["a_year"],
                     a_est=request.POST["a_est"]
                     )
        autobd.save()
        return render(request, 'folders/fautos.html')
    return render(request, 'folders/fautos.html')

def users(request):
    if request.method=="POST":
        usersbd= Users(user_name=request.POST["user_name"],
                       user_pass=request.POST["user_pass"],
                       user_mail=request.POST["user_mail"],
                       user_age=request.POST["user_age"],
                       user_est=request.POST["user_est"]
                       )
        usersbd.save()
        return render(request, 'folders/fusers.html')
    return render(request, 'folders/fusers.html')
