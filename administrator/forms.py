from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm



class UserCreationForm2(UserCreationForm):

	class Meta:
		model = User
		fields = [
		'username',
		'password1',
		'password2',
		'email',
		'first_name',
		'last_name',
		]
