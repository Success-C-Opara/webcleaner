from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.models import User
from django import forms 



class Regg(UserCreationForm):
      email = forms.EmailField(required=True,)
      username = forms.CharField(required=True,)
      password1 = forms.CharField(required=True,)
      password2 = forms.CharField(required=True,)

      class Meta:
            model = User
            fields = ("email","username","password1","password2")

      def save(self,commit=True):
          user = super(Regg,self).save(commit=False)
          user.email = self.cleaned_data['email']
          if commit:
             user.save()
          return user 



