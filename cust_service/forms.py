from django import forms
from .models import ServiceRequest, ServiceRequestType

class ServiceRequestForm(forms.ModelForm):
    request_type = forms.ModelChoiceField(
    queryset=ServiceRequestType.objects.all(),
    empty_label="Select Request Type" 
    )
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'details', 'files']

