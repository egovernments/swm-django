from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Ward
from django.db import models
from events.models import Location

class Wardform(forms.ModelForm):

	wards = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            queryset=Location.objects.all())

	class Meta:
		model = Ward
		fields = [
		'wards'
		]


# def clean_username(self):
# 	username = self.cleaned_data['username']
# 	user_exists = User.objects.get(username=username)
# 	if user_exists:
# 		raise ValidationError("User exists")


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

	def clean_username(self):
		username = self.cleaned_data('username')
		user_exists = User.objects.get(username=username)
		if user_exists:
			raise forms.ValidationError("User exists")
