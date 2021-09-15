from pprint import pprint
from API.models import CustomUser
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.edit import UpdateView
from .eia_app import get_eia_data
from .nrel_app import get_nrel_data
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from django.contrib.auth.views import LoginView
from .forms import ProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
class Index(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            geocoder = Nominatim(user_agent='solar_power')
            geocode = RateLimiter(geocoder.geocode, min_delay_seconds = 1,   return_value_on_exception = None) 
            location = geocode(request.user.address1)
            context = get_eia_data(request.user.state)
            context['annual_ghi'] = get_nrel_data(location.latitude,location.longitude)
            context['range'] = range(len(context['year']))
            context['historical_data'] = zip(context['year'],context['price'])
            pprint(context, indent=2)
            return render(request, 'index.html',context)
        else:
            return HttpResponse('Not logged in. Login coming soon')

class Splash(LoginView):
    template_name = 'splash.html'

class Profile(LoginRequiredMixin,UpdateView):
    model = CustomUser
    form_class = ProfileForm
    template_name = 'profile.html'
    def get_success_url(self):
        return reverse_lazy('index')

    
