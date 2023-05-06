from django.shortcuts import render
from django.http import HttpResponse

# Create your views function here.
# create a def home which will send a request
# the request has to be send in a respond format httpResponse( for static)
# use render to call the index.html, this is for dynamic

def home(request):
    #return render(request, 'index.html') # for dynamic template
    return render(request, 'index.html',{'name':'Ako'}) # for dynamic data like name etc

def add(request):
    # using value to send request to the server and we need to get a response from the server
    val1 = int(request.POST["num1"]) # use integer to convert string to int
    val2 = int(request.POST["num2"]) # in order to prevent cyber attack we use POST which is secure instead of GET
    res = val1 + val2
    return render(request, "result.html",{'result':res}) # create a function to add the sum
   


