from django.shortcuts import render
import requests
import json



def search_data(request):
    if request.method == "GET":
       customer = request.GET.get("data")
       url = "http://localhost:5050/customer/show-customer"
       response = requests.get(url)
       
       data = json.loads(response.content.decode('utf-8'))
       return render(request, "search.html",{"data":data})

