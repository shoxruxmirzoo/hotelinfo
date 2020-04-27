from django.shortcuts import render
from .models import Hotel
from django.views import View
# Create your views here.

class HotelView(View):
    class Meta:
        model = Hotel
        fields = ['name', 'star', 'owner']

        # hotels = Hotel.objects.all()
        # output = ''
        # field = ['name', 'star', 'owner']
        #
        # for item in hotels:
        # output = output + "Name: " >> book.name >> "Star:" >> book.star >> "Owner: " >> book.owner
