import random
from django.shortcuts import render
import random

def home(request):
	return render(request, 'generator/home.html')

def about(request):
	return render(request, 'generator/about.html')

def password(request):
	chars = list('abcdefghijklmnopqrstuvwxyz')

	if request.GET.get('number'):
		chars.extend(list('0123456789'))

	if request.GET.get('uppercase'):
		chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

	if request.GET.get('special'):
			chars.extend(list('!@#$%^&*()+_=~'))
	

	length=int(request.GET.get('passlen', 10))

	generated_password=''

	for i in range(length):
		generated_password += random.choice(chars)
	return render(request, 'generator/password.html', {'password': generated_password})