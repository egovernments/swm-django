from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from accounts.forms import UserCreationForm2, Wardform
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Ward

def my_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		form2= Wardform(request.POST)
		if form.is_valid():
			user = form.save(commit = False)
			ward = form2.save(commit = False)
			user.save()
			print(user)
			ward.user = user
			ward.save()
			print(ward)
			return redirect('/accounts/login')
		else:
			message = "fill all the fields"
			args = {'form': form, 'form2': form2, 'message':message}
			return render(request, 'accounts/reg_form.html', args)
	else:
		form = UserCreationForm2()
		form2 = Wardform()
		message = ""
		args = {'form': form, 'form2': form2, 'message':message}
		return render(request, 'accounts/reg_form.html', args)

@login_required
def editpref(request):
	user = request.user
	ward = Ward.objects.all().filter(user = user)[0]
	if request.method == 'POST':
		form2= Wardform(request.POST, instance=ward)
		if form2.is_valid():
			form2.save()
			return redirect('/events')
		else:
			args = {'form2': form2}
			return render(request, 'accounts/edit.html', args)
	else:
		form2 = Wardform(instance=ward)
		args = {'form2': form2}
		return render(request, 'accounts/edit.html', args)
