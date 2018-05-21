from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import firstruc
from .forms import fir_form
from django import forms
from police.sms import SMS
from police.models import RPF
# Create your views here.

def firform(request):
    form = fir_form(request.POST or None)
    if form.is_valid():
        cleanpnr=form.cleaned_data['pnr']
        cleanphone=form.cleaned_data['phone']
        all_forms = firstruc.objects.all()
        for i in all_forms:
            if(cleanpnr==i.pnr and cleanphone==i.phone):
                return render(request, 'fir/firform.html',{"form": form})
        instance = form.save(commit=False)
        a = RPF.objects.get(pnr=cleanpnr)
        rpfphone = a.phone
        SMS("You have been assigned to check the case for Mobile No. +91"+str(cleanphone), str(rpfphone))
        instance.save()

        return HttpResponseRedirect('/')

    context = {
        "form": form,
    }
    return render(request, 'fir/firform.html',context)
