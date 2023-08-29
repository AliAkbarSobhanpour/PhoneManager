from django import forms 
from .models import PhoneModel, Brand


class PhoneForm(forms.ModelForm):
    
    class Meta:
        model = PhoneModel
        fields = "__all__"
        
    def clean(self):
        
        # cleaned data variables ---------------------------------------------------------------------------------------+
        
        cleaned_data = super().clean()
        count = cleaned_data.get("count")
        availability = cleaned_data.get("availability")
        phone_model = cleaned_data.get("phone_model")
        color = cleaned_data.get("color")
        creator_country = cleaned_data.get("creator_country")
        
        # end -----------------------------------------------------------------------------------------------------------
        
        # validate for availability ------------------------------------------------------------------------------------+
        
        if availability == True:
            if count == 0:
                self.add_error("count", "باید تعداد محصولات بیشتر از 0 باشد")        
                
        # end -----------------------------------------------------------------------------------------------------------
        
        # validate for existing ----------------------------------------------------------------------------------------+
         
        is_exist = PhoneModel.objects.filter(
            phone_model__iexact = phone_model,
            color__iexact = color,
            creator_country__iexact = creator_country     
        ).exists()
        
        if is_exist:
            raise forms.ValidationError("محصول مورد نظر موجود است")    
        
        # end ------------------------------------------------------------------------------------------------------------    
        return cleaned_data
        
        
class BrandForm(forms.ModelForm):
    
    class Meta:
        model = Brand
        fields = "__all__"

    
    def clean(self):
        cleaned_data = super().clean()
        
        brand_name = cleaned_data.get("brand_name")
        brand_national = cleaned_data.get("brand_national")
        
        is_exist = Brand.objects.filter(
            brand_name__iexact = brand_name,
            brand_national__iexact = brand_national
        ).exists()
        
        if is_exist:
            raise forms.ValidationError("برند مد نظر موجود است، لطفا از میان برند ها انتخاب بکنید.")
        
        return cleaned_data
    