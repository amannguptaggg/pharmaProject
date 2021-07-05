from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from .forms import LoginForm, RegistrationForm
from .models import Users
from django.contrib import messages

siteName = 'Pharmaa'

def index(request):
    allUsers = Users.objects.all()

    context ={
        'title':'Home | '+siteName,
        'allUsers':allUsers
    }
    return render(request,'main/core/index.html',context)
    

def registration(request):
    myData = ''
    registrationForm = RegistrationForm()
    if request.method == 'POST':
        registrationForm = RegistrationForm(request.POST)
        if registrationForm.is_valid():
            registrationForm.save()
            myData = 'Logged In'
            
            
            
    return render(request,'main/core/registration.html',context={'title':'Registration | '+siteName,'form': registrationForm,
    'formData' : myData
    })

def login(request):
    loginForm = LoginForm()
    userLoginId = ''
    userLoginPassword = ''
    msg = ''
    userID = ''
    passw = 'no'

    if request.method == 'POST' or None:
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            userLoginId = loginForm.cleaned_data['userLoginId']
            userLoginPassword = loginForm.cleaned_data['userLoginPassword']

            try:
                userID =   Users.objects.get(Q(email=userLoginId) | Q(username=userLoginId) | Q(phone_number = userLoginId))

                if (((userLoginId == userID.username) or (userLoginId == userID.email) or (userLoginId == userID.phone_number)) and (userLoginPassword == userID.password)):
                    messages.success(request,'Successfuly Logged In')
                else:
                    messages.error(request,'User Id or Password Incorrect')
            except:
                messages.error(request,'User ID does not exist. Sign Up for new account!')

            
    
    context={
        'title':'Login | '+siteName,
        'form': loginForm,
        'userLoginName':userLoginId,
        'userLoginPass':userLoginPassword,
        'userID':userID,
        'passw':passw,
        }



    return render(request,'main/core/login.html',context)



def about(request):
    return render(request,'main/general/about.html')

def contact(request):
    return render(request,'main/general/contact.html')
