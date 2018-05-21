from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import policelogin, constableattend
from fir.models import firstruc
from fir.forms import fir_form
from .models import RPF
from .sms import SMS

# Create your views here.
def attendance(request):
    form = constableattend()
    if request.method == 'POST':
        form = constableattend(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    return render(request, 'police/constable.html', {"form": form})

def login(request):
    form = policelogin()
    if request.method == 'POST':
        form = policelogin(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            return responselist(request, user)
    return render(request, 'police/policeadmin.html',{"form": form})

def responselist(request, user):
    all_forms = firstruc.objects.all()
    all_constables = RPF.objects.all()
    context = {"all_forms": all_forms, "user": user, "all_constables": all_constables}
    return render(request, 'police/responselist.html', context)

def firdisplay(request,phoneno):
    all_forms = firstruc.objects.all()
    for form in all_forms:
        if form.phone == phoneno:
            break
    context = {
        'form': form,
    }
    if request.method=='POST':
        form = fir_form(request.POST)
        firstruc.objects.filter(phone=phoneno).update(status='Resolved')
        context = {
            'form': form,
        }
        SMS("Dear Passenger, your complaint has been resolved.",str(phoneno))
        return HttpResponseRedirect('/')
    return render(request, 'police/resolve.html', context)
