import random
from django.shortcuts import render


def home(request):
	num = random.randint(1, 100000000)
	context = {
		"context_variable": "Omer Zaheer",
		"num": num
	}
	return render(request, "base.html", context)
