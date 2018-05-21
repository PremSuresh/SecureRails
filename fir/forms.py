from django import forms
from .models import firstruc
import geocoder
class fir_form(forms.ModelForm):
    class Meta:
        var = [

        ("GRP", "GRP(Law & Order)"),
        ("RPF", "RPF(Theft)"),
        ]
        model = firstruc
        widgets = {
            'pnr': forms.TextInput(attrs={'placeholder': 'PNR'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone'}),
            'type': forms.Select(choices=(var)),
            'complaint': forms.Textarea(attrs={'cols': 50, 'rows': 8, 'placeholder': 'COMPLAINT'}),
        }
        labels = {
            'pnr': (''),
            'phone': (''),
            'type': (''),
            'complaint': (''),
        }
        fields = ['pnr', 'phone', 'type', 'complaint',]
