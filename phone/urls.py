from django.urls import path
from . import views

urlpatterns = [
    path("", views.PhoneListView.as_view(), name="phone-list-page"),
    path("create-phone", views.phone_form_view, name="phone-form-page"),
    path("create-brand", views.brand_form_view, name="brand-form-page")
]