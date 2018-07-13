from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return redirect('/accounts/login')
