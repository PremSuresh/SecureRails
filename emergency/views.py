from django.shortcuts import render
from .forms import regform,emergencyform
from .models import registersos
from police.sms import SMS
from django.http import HttpResponseRedirect
import geocoder
# Create your views here.
def registers(request):
    form = regform(request.POST or None)
    all_forms = registersos.objects.all()
    if form.is_valid():
        cleanphone=form.cleaned_data['phone']
        for i in all_forms:
            if(cleanphone==i.phone):
                return render(request, 'emergency/register.html',{"form": form})
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/')
    return render(request,'emergency/register.html', {"form": form})

def alert(request):
    form = emergencyform()
    if request.method == 'POST':
        form = emergencyform(request.POST)
        if form.is_valid():
            cleanphone = form.cleaned_data['phone']
            reg = registersos.objects.get(phone=cleanphone)
            lat = str(geocoder.ip('me').latlng[0])
            lng = str(geocoder.ip('me').latlng[1])
            SMS("Your friend +91"+ cleanphone+ " is in distress at lat:"+lat+" long:"+ lng, reg.phone1)
            SMS("Your friend +91"+ cleanphone+ " is in distress at lat:"+lat+" long:"+ lng, reg.phone2)
            SMS("Your friend +91"+ cleanphone+ " is in distress at lat:"+lat+" long:"+ lng, reg.phone3)
            return HttpResponseRedirect('/')
    return render(request,'emergency/alert.html', {'form': form})
