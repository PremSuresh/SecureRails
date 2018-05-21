from django import forms
from .models import registersos



class regform(forms.ModelForm):
    class Meta:
        model = registersos
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': 'Your number'}),
            'phone1': forms.TextInput(attrs={'placeholder': 'Phone Number 1'}),
            'phone2': forms.TextInput(attrs={'placeholder': 'Phone Number 2'}),
            'phone3': forms.TextInput(attrs={'placeholder': 'Phone Number 3'}),
        }
        labels = {
            'phone': (''),
            'phone1': (''),
            'phone2': (''),
            'phone3': (''),
        }
        fields = ['phone', 'phone1', 'phone2', 'phone3',]
class emergencyform(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone number'}), label='')
    def clean(self):
        cleanphone = self.cleaned_data['phone']
        try:
            p = registersos.objects.get(phone=cleanphone)
        except registersos.DoesNotExist:
            raise forms.ValidationError("No such number")
