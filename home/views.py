from django.shortcuts import render
from .models import userModel
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'About.html',{'ttmUsers' : userModel.objects.all()})
def contact(request):
    return render(request,'Contact.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        return render(request,'index.html')
    return render(request,'Login.html')
def services(request):
    return render(request,'Services.html')
# Create your views here.
