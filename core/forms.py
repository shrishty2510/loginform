
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

from core.models import SignUp


user_choices = [
    ('Doctor','Doctor'),
    ('Patient','Patient')
]

 
class Extenduser(forms.ModelForm):
   user_type=forms.ChoiceField(choices=user_choices,widget=forms.RadioSelect())
 
   class Meta :
       model = SignUp
       fields = '__all__'
       exclude=['user']
       labels = {'pin':'Pin Code' ,'profile_image':'Profile Image',}

       widgets = {
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'pin':forms.TextInput(attrs={'class':'form-control'}),
            'user_type':forms.TextInput(attrs={'class':'form-control'}),
            'profile image':forms.TextInput(attrs={'class':'form-control'}),
       }
            
class MainUser(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),help_text=('enter a vaild password'),label='Password')
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),help_text=('enter the above password'),label='Confirm Password')

    class Meta:
        model = User
        fields = ['first_name','last_name','email','username']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            
       }



class Signin_form(forms.Form):
    Username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control my-2','placeholder':'Enter Your Username Here'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control my-2','placeholder':'Enter Your Password Here'}))




       
    

















































      