from django.shortcuts import render
import requests
from django.http import HttpResponse
# Create your views here.
def home(request):
	url="https://api.coingecko.com/api/v3/coins/markets?vs_currency=INR&order=market_cap_desc&per_page=100&page=1&sparkline=false"
	r = requests.get(url).json()
	context = {'data': r}
	return render(request, 'positions/index.html', context)
	#return HttpResponse(r)