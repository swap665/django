from django.shortcuts import render,HttpResponse

# Create your views here.
def index(requests):
    return render(requests,"user.html")