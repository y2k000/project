from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserDetails
from django.forms import ModelForm

class CreateUserProf(ModelForm):
    class Meta:
        model =  UserDetails
        fields = ['mobile','user_profile_picture']        

class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','first_name','last_name']
        
