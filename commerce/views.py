from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'commerce/home.html')

def cart(request):
	return render(request, 'commerce/cart.html')

def checkout(request):
	return render(request, 'commerce/checkout.html')