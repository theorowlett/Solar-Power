from django.forms import ModelForm, Textarea
from API.models import CustomUser

class ProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','address1','address2','state','zip']