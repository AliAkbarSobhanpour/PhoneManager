from django.urls import path
from . import views

urlpatterns = [
    path("", views.PhoneListView.as_view(), name="phone-list-page"),
]
