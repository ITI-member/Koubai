from django import forms
from .models import DeptMaster

class DeptCreateForm(forms.ModelForm):
    
    class Meta:
        model = DeptMaster
        fields = '__all__'
