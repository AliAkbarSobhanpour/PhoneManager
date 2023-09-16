from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"phonemodel", views.PhoneModelViewSet)


urlpatterns = [
    path("", views.PhoneListView.as_view(), name="phone-list-page"),
    path("create-phone", views.phone_form_view, name="phone-form-page"),
    path("create-brand", views.brand_form_view, name="brand-form-page"),
    path("api/", include(router.urls))
]