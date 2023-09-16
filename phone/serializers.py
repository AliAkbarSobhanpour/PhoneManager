from .models import PhoneModel, Brand

from rest_framework import serializers


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["brand_name", "brand_national"]

class PhoneModelSerializer(serializers.ModelSerializer):
    phone_brand = BrandSerializer()
    class Meta: 
        model = PhoneModel
        fields = "__all__"

