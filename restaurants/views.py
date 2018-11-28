import random
from django.shortcuts import render


def home(request):
	num = random.randint(1, 100000000)
	context = {
		"context_variable": "Omer Zaheer",
		"num": num
	}
	return render(request, "home.html", context)


def contact(request):
	context = {}
	return render(request, "contact.html", context)


def about(request):
	context = {}
	return render(request, "about.html", context)
