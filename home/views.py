from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth  import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request, 'home.html')

def handleSignup(request):
    # get the post parameters
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']
        pass2 = request.POST['pass2']
        dob = request.POST['dob']
        img = request.POST['img']


      
        # create the user
        myuser = User.objects.create_user(username,password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.dob = dob
        myuser.img = img
        myuser.save()
        messages.success(request,f"Congratulations, {myuser} your FOODieWay account is created successfully!")
        return redirect('/')
    else:
        return HttpResponse('404-page not found')

def handeLogin(request):
    if request.method =='POST':
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        myuser=authenticate(username= loginusername, password= loginpassword)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, f"{myuser} ,Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request, "Invalid user! Please try again after some time")
            return redirect('/')

    return HttpResponse("404- Not found")
   

    return HttpResponse("login")
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

 