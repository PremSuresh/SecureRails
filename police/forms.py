from django import forms
from .models import policeuser,RPF

class policelogin(forms.Form):
    user = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'USERNAME'}), label='')
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}), label='')
    def clean(self):
        cleanuser = self.cleaned_data['user']
        cleanpass = self.cleaned_data['password']
        try:
            p = policeuser.objects.get(user=cleanuser, password=cleanpass)
        except policeuser.DoesNotExist:
            raise forms.ValidationError("No such police user")

class constableattend(forms.ModelForm):
    class Meta:
        model = RPF
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'PHONE'}),
            'pnr': forms.TextInput(attrs={'placeholder': 'PNR'}),
        }
        labels = {
            'name': (''),
            'phone': (''),
            'pnr': (''),
        }
        fields = ['name', 'phone', 'pnr']
    def clean(self):
        cleanname = self.cleaned_data['name']
        cleanphone = self.cleaned_data['phone']
        cleanpnr = self.cleaned_data['pnr']
        try:
            p = RPF.objects.get(pnr=cleanpnr)
        except RPF.DoesNotExist:
            raise forms.ValidationError("No such PNR")
        RPF.objects.filter(pnr=cleanpnr).update(name=cleanname,pnr=cleanpnr,phone =cleanphone)
