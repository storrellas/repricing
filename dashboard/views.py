from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    #return HttpResponse("return this string")
    return render(request, "dashboard.html")