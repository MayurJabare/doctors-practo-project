from django import forms
from .models import DoctorInfo

class DoctorFilterForm(forms.Form):
    specialty = forms.ChoiceField(choices=[], required=False, label='Specialty')
    locality = forms.ChoiceField(choices=[], required=False, label='Locality')

    def __init__(self, *args, **kwargs):
        super(DoctorFilterForm, self).__init__(*args, **kwargs)
        self.fields['specialty'].choices = [('', 'All Specialties')] + [(specialty, specialty) for specialty in DoctorInfo.objects.values_list('specialty', flat=True).distinct()]
        self.fields['locality'].choices = [('', 'All Localities')] + [(locality, locality) for locality in DoctorInfo.objects.values_list('locality', flat=True).distinct()]