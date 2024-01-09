from django.shortcuts import render,redirect
from .models import userModel
from django.contrib import messages

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'About.html')
def contact(request):
    return render(request,'Contact.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = userModel.objects.filter(username=username,password=password)
        if user:
            return render(request,'about.html',{'ttmUsers' : user})
        return render(request,'index.html')
    return render(request,'Login.html')
def services(request):
    return render(request,'Services.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        print(username,password,email,name,age,gender,phone)
        # Create a new user object
        user = userModel(username=username, password=password, email=email, name=name, age=age, gender=gender, phone=phone)
        
        # Save the user object
        user.save()
        
        # Add a flash message
        messages.success(request, 'Account created. Please login.')
        
        return render(request,'login.html')
        
    return render(request,'register.html')
# Create your views here.
