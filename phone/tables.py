from django_tables2 import tables
from .models import PhoneModel


class PhoneTable(tables.Table):
    class Meta:
        model = PhoneModel
        template_name = "django_tables2/bootstrap.html"
