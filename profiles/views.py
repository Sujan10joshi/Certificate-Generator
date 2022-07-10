from email.policy import default
from django.shortcuts import render
from django.http import HttpResponseRedirect
from profiles.models import User
from .forms import UserAdd

# Create your views here.


def show_profile(request):
    fm = UserAdd()
    usrdetails = User.objects.latest('id')
    return render(request, 'profiles/showprofiles.html', {'usrdetail': usrdetails})


def add_user(request):
    if request.method == "POST":
        fm = UserAdd(request.POST)
        if fm.is_valid():
            fn = fm.cleaned_data['first_name']
            mn = fm.cleaned_data['middle_name']
            ln = fm.cleaned_data['last_name']
            cn = fm.cleaned_data['contact_number']
            ad = fm.cleaned_data['address']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(first_name=fn, middle_name=mn, last_name=ln,
                       address=ad, contact_number=cn, email=em, password=pw)
            reg.save()
            return HttpResponseRedirect('/form/success/')
    else:
        fm = UserAdd()
    return render(request, 'profiles/add_user.html', {'form': fm})
