from django import forms 
from .models import PhoneModel, Brand



class PhoneForm(forms.ModelForm):
    
    class Meta:
        model = PhoneModel
        fields = "__all__"
        
    def clean(self):
        cleaned_data = super().clean()
        count = cleaned_data.get("count")
        availability = cleaned_data.get("availability")
        
        if availability == True:
            if count == 0:
                self.add_error("count", "باید تعداد محصولات بیشتر از 0 باشد")        
        
        
        return cleaned_data
        
        
class BrandForm(forms.ModelForm):
    
    class Meta:
        model = Brand
        fields = "__all__"

    