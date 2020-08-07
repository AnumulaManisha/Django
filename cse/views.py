from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import *
from django.http import HttpResponse

from .models import Placement, Feedback, ImagesUpload
# Create your views here.
def index(request):
    return render(request, 'homepage.html')
def about(request):
    return render(request, 'About.html')
def achieve(request):
    return render(request, 'Achievements.html')
def contact(request):
    return render(request, 'ContactUs.html')
def placement(request):
    #p1 = Placement()
    #p1.companyname = 'Google'
    #p1.package = 5000000
    #p1.no_of_stud = 2

    p = Placement.objects.all()
    return render(request, 'PlacementInfo.html', {'p':p})
def faculty(request):
    return render(request, 'Facultydetails.html')
def Studentportal(request):
    return render(request,'Studentportal.html')
def Studlogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/cse/Studentlogin/Studentportal')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('/cse/Studentlogin')
    else:
        return render(request, 'Studentlogin.html')
def Studsignup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                #print('Username taken')
                messages.info(request,'Username taken')
                return redirect('/cse/Studentlogin/Studentsignup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('/cse/Studentlogin/Studentsignup')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('User created')
                return redirect('/cse/Studentlogin')
        else:
            messages.info(request,'Passwords not matching')
            return redirect('/cse/Studentlogin/Studentsignup')
        #return redirect('/cse')
    else:
        return render(request, 'Studentsignup.html')
def logout(request):
    auth.logout(request)
    return redirect('/cse/Studentlogin')
def Attendance(request):
    return render(request,'Attendance.html')
def Timetable(request):
    return render(request,'Timetable.html')
def FeedbackForm(request):
    if request.method == 'POST':
        if request.POST.get('userName') and request.POST.get('userEmail') and request.POST.get('subject') and request.POST.get('content'):
            post = Feedback()
            post.userName = request.POST.get('userName')
            post.userEmail = request.POST.get('userEmail')
            post.subject = request.POST.get('subject')
            post.content = request.POST.get('content')
            post.save()

        return redirect('/cse/Studentlogin/Studentportal')
    else:
        return render(request,'FeedbackForm.html')
def Teacherlogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/cse/Teacherlogin/Teacherportal')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('/cse/Teacherlogin')
    else:
       return render(request, 'Teacherlogin.html')
#def Teachersignup(request):
 #   if request.method == 'POST':
  #      if request.POST.get('email') and request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('password1') and request.POST.get('password2'):
   #         p = Tsignup()
    #        p.firstname = request.POST.get('firstname')
     #       p.lastname = request.POST.get('lastname')
      #      p.email = request.POST.get('email')
       #     p.password1 = request.POST.get('password1')
        #    p.password2 = request.POST.get('password2')
#
 #           if p.password1 == p.password2:
  #                  p.save()
   #                 print('User created')
    #                return redirect('/cse/Teacherlogin')
     #       else:
      #          messages.info(request,'Passwords not matching')
       #         return redirect('/cse/Teacherlogin/Teachersignup')
    #else:
     #   return render(request, 'Teachersignup.html')
def Teachersignup(request):
        if request.method == "POST":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    # print('Username taken')
                    messages.info(request, 'Username taken')
                    return redirect('/cse/Teacherlogin/Teachersignup')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Email taken')
                    return redirect('/cse/Teacherlogin/Teachersignup')
                else:
                    user = User.objects.create_user(username=username, password=password1, email=email,
                                                    first_name=first_name, last_name=last_name)
                    user.save()
                    print('User created')
                    return redirect('/cse/Teacherlogin')
            else:
                messages.info(request, 'Passwords not matching')
                return redirect('/cse/Teacherlogin/Teachersignup/')
            # return redirect('/cse')
        else:
            return render(request, 'Teachersignup.html')
def Teacherlogout(request):
    auth.logout(request)
    return redirect('/cse/Teacherlogin')
def Teacherportal(request):
    return render(request,'Teacherportal.html')
#def upload(request):
 #   if request.method == 'POST':
  #      if request.POST.get('subject') and request.POST.get('semester') and request.POST.get('description') and request.POST.get('image'):
   #         post = ImagesUpload()
    #        post.subject = request.POST.get('subject')
     #       post.semester = request.POST.get('semester')
    #        post.description = request.POST.get('description')
     #       post.image = request.POST.get('image')
      #      post.save()
       #     print('Data entered')
        #return redirect('/cse/Teacherlogin/Teacherportal')
    #else:
     #   return render(request,'upload.html')

def upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/cse/Teacherlogin/Teacherportal')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form })
def UploadDisplay(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        uploads = ImagesUpload.objects.all()
        return render(request, 'UploadDisplay.html',{'upload_images': uploads})




