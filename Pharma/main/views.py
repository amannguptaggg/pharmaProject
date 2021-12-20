from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from .forms import LoginForm, RegistrationForm
from .models import Users
from django.contrib import messages

siteName = 'PharmaEdu'
username = None

def index(request):
    allUsers = Users.objects.all()
    if request.session.has_key('username'):
        username = request.session['username']
    else:
        username = None

    context ={
        'title':'Home | '+siteName,
        'allUsers':allUsers,
        'username' : username
    }
    return render(request,'main/core/index.html',context)
    

def registration(request):
    myData = ''
    username = None

    registrationForm = RegistrationForm()
    if request.method == 'POST':
        registrationForm = RegistrationForm(request.POST)
        if registrationForm.is_valid():
            registrationForm.save()

            return redirect('login')
            
    return render(request,'main/core/registration.html',
    context={'title':'Registration | '+siteName,'form': registrationForm,
    'formData' : myData,
    'username' : username
    })

def login(request):
    loginForm = LoginForm()
    userLoginId = ''
    userLoginPassword = ''
    userID = ''
    passw = 'no'
    loggedIn = False
    username = None

    if request.method == 'POST' or None:
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            userLoginId = loginForm.cleaned_data['userLoginId']
            userLoginPassword = loginForm.cleaned_data['userLoginPassword']

            try:
                userID =   Users.objects.get(Q(email=userLoginId) | Q(username=userLoginId) | Q(phone_number = userLoginId))

                if (((userLoginId == userID.username) or (userLoginId == userID.email) or (userLoginId == userID.phone_number)) and (userLoginPassword == userID.password)):
                    request.session['username'] = userLoginId
                    if request.session.has_key('username'):
                        username = request.session['username']
                    else:
                        username = None   
                    # messages.success(request,'Successfuly Logged In')
                    # loggedIn = True
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
        'username' : username
        # 'loggedIn' : loggedIn
        }



    return render(request,'main/core/login.html',context)




def about(request):
    username = None
    if request.session.has_key('username'):
        username = request.session['username']
    else:
        username = None
    context = {
        'username' : username
    }
    return render(request,'main/general/about.html', context= context)



def contact(request):
    username = None
    if request.session.has_key('username'):
        username = request.session['username']
    else:
        username = None
    
    context = {
        'username' : username
    }
    return render(request,'main/general/contact.html', context = context)



def courses(request):
    username = None
    if request.session.has_key('username'):
        username = request.session['username']
    else:
        username = None
    
    context = {
        'username' : username
    }
    return render(request,'main/general/courses.html', context= context)



def logout(request):
    if request.session.has_key('username'):
        request.session.flush()
    return redirect('login')