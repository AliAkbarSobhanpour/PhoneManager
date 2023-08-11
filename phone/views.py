from django.views.generic.list import ListView
from django.shortcuts import render
from .models import PhoneModel
from django.core.exceptions import ValidationError
from django.db.models import F, Q
# Create your views here.


class PhoneListView(ListView):
    model = PhoneModel
    context_object_name="phones"
    template_name='phone/phones-list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()

        # self.request.GET
        nationality = self.request.GET.get("nationality")
        same_nationality = self.request.GET.get("same_nationality")
        availability = self.request.GET.get("availability")
        brand_things = self.request.GET.get("brand_things")
        
        # filter based on brand name and phone model ---------------------------------------------------------------------+
        if brand_things:
            brand_things = brand_things.replace("+", " ")
            queryset = queryset.filter(Q(phone_brand__brand_name__iexact=brand_things)|Q(phone_model__icontains=brand_things))
            
        # end -------------------------------------------------------------------------------------------------------------
        
        # filter based on nationality -------------------------------------------------------------------------------------+
        
        if nationality is not None:
            queryset = queryset.filter(phone_brand__brand_national=nationality)
        
        # end --------------------------------------------------------------------------------------------------------------
         
        # filter based on  brand_nationality == creator_country -----------------------------------------------------------+
        
        if same_nationality == "on":
            queryset = queryset.filter(phone_brand__brand_national__iexact = F("creator_country") )
        
        # end --------------------------------------------------------------------------------------------------------------
        
        # only phones that are available ----------------------------------------------------------------------------------+
        
        if availability == "on":
            queryset = queryset.filter(availability=True)
            
        # end --------------------------------------------------------------------------------------------------------------
        
            
        
        
        print(self.request.GET)    
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # get nationality's and send it to template ------------------------------------------------------------------------+
        
        list_national = set([x.phone_brand.brand_national for x in PhoneModel.objects.all()])
        context["nationals"] = list_national
        
        # end ---------------------------------------------------------------------------------------------------------------
        return context
    
    
