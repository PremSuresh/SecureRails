from django import forms
from fir.models import firstruc

class pnr_form(forms.Form):
    pnr = forms.CharField(label ='', widget=forms.TextInput(attrs={'placeholder': 'PNR'}))
    phone = forms.CharField(label ='', widget=forms.TextInput(attrs={'placeholder': 'Phone'}), max_length=10)
    def clean(self):
        cleanpnr=self.cleaned_data['pnr']
        cleanphone = self.cleaned_data['phone']
        try:
            p = firstruc.objects.get(pnr=cleanpnr,phone=cleanphone)
        except firstruc.DoesNotExist:
            raise forms.ValidationError("No such complaint")
