from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class PhoneModel(models.Model):
    phone_brand = models.ForeignKey('Brand', on_delete=models.CASCADE, verbose_name="برند")
    phone_model = models.CharField("مدل تلفن همراه", max_length=300 ,unique=True)
    price = models.IntegerField("قیمت", default=0, validators=[
        MinValueValidator(0, "مقدار مورد نظر باید بیشتر از 0 باشد")
    ])
    color = models.CharField("رنگ محصول",max_length=200)
    phone_size = models.FloatField("سایز گوشی همراه", default=0, validators=[
        MinValueValidator(0, "مقدار مورد نظر باید بیشتر از 0 باشد.")
    ])
    availability = models.BooleanField("موجود", default=False)
    count = models.IntegerField("تعداد",blank=True, default=0, validators=[
        MinValueValidator(0, "مقدار مورد نظر باید بیشتر از 0 باشد")
    ])
        
    creator_country = models.CharField("کشور سازنده", max_length=300)

    
    def __str__(self):
        return self.phone_model
    
    class Meta:
        db_table = 'phone'
        verbose_name = 'گوشی'
        verbose_name_plural = 'گوشی ها'
    

class Brand(models.Model):
    brand_name = models.CharField("نام برند" ,max_length=300)
    brand_national = models.CharField("ملیت برند", max_length=300)
    
    
    def __str__(self):
        return self.brand_name
    
    class Meta:
        db_table = 'brand'
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'