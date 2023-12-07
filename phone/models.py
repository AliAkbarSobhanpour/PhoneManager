from django.db import models
from django.core.validators import MinValueValidator
from django_countries.fields import CountryField


# Create your models here.
class PhoneModel(models.Model):
    phone_brand = models.ForeignKey('Brand', on_delete=models.CASCADE, verbose_name="برند")
    phone_model = models.CharField("مدل تلفن همراه", max_length=300, unique=True)
    price = models.IntegerField("قیمت", default=0, validators=[
        MinValueValidator(1, "قیمت را به درستی وارد بکنید")
    ])
    color = models.CharField("رنگ محصول", max_length=200)
    phone_size = models.FloatField("سایز گوشی همراه", default=0, validators=[
        MinValueValidator(1, " اندازه صفحه نمایش را به درستی وارد کنید ")
    ])
    availability = models.BooleanField("موجود", default=False)
    count = models.IntegerField("تعداد", blank=True, default=0, validators=[
        MinValueValidator(0, "تعداد گوشی ها را به درستی وارد بکنید")
    ])

    creator_country = CountryField("کشورسازنده")

    total_price = models.IntegerField("جمع قیمت محصولات", validators=[
        MinValueValidator(0, "قیمت کل را به درستی وارد بکنید ")
    ])

    def save(self, *args, **kwargs):
        self.total_price = self.price * self.count
        super(PhoneModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.phone_model

    class Meta:
        db_table = 'phone'
        verbose_name = 'گوشی'
        verbose_name_plural = 'گوشی ها'


class Brand(models.Model):
    brand_name = models.CharField("نام برند", max_length=300)
    brand_national = CountryField("ملیت برند")

    def __str__(self):
        return self.brand_name

    class Meta:
        db_table = 'brand'
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'
