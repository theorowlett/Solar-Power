from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from geopy.location import Location
from API.models import CustomUser
from django.views.generic.base import View
from .eia_app import get_data
from .nrel_app import get_nrel_data
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            geocoder = Nominatim(user_agent='solar_power')
            geocode = RateLimiter(geocoder.geocode, min_delay_seconds = 1,   return_value_on_exception = None) 
            location = geocode(request.user.address1)
            annual_ghi = get_nrel_data(location.latitude,location.longitude)
            context = {
                'annual_ghi': annual_ghi,
            }
            return render(request, 'index.html',annual_ghi)
        else:
            return HttpResponse('Not logged in. Login coming soon')
    
