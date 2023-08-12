from django import forms 
from .models import PhoneModel, Brand

class PhoneForm(forms.ModelForm):
    
    class Meta:
        model = PhoneModel
        fields = "__all__"


class BrandForm(forms.ModelForm):
    
    class Meta:
        model = Brand
        fields = "__all__"

    