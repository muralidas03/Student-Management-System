from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

from StudentApp.models import Course, Student


# Create your views here.
@login_required
def homePage(request):
    students = Student.objects.all()
    return render(request,'homePage.html',{'studentsData':students, 'count' : len(students) })

@login_required
def home(request):
    if request.method == 'POST':
        s = Student()
        s.Name = request.POST['tname']
        s.Course = Course.objects.get(CourseName=request.POST['tcourse'])
        s.phoneNo = request.POST['tphone']
        s.Email = request.POST['tmail']
        s.Age = request.POST['tage']
        s.save()
        return redirect(homePage)
    else:
        courses = Course.objects.all()
        data = {'courses' : courses}
        return render(request,'userDetails.html',data)

@login_required
def editDetails(request,id):
    s = Student.objects.get(id=id)
    if request.method == 'POST':
        s.Name = request.POST['tname']
        s.Course = Course.objects.get(CourseName=request.POST['tcourse'])
        s.phoneNo = request.POST['tphone']
        s.Email = request.POST['tmail']
        s.Age = request.POST['tage']
        s.save()
        return redirect(homePage)
    else:
        courses = Course.objects.all()
        return render(request,'edit.html',{'student':s,'courses':courses})

@login_required
def deleteDetails(request,id):
    s = Student.objects.get(id=id)
    s.delete()
    return redirect(homePage)

@login_required
def dummy(request):
    return render(request,'index.html')

@never_cache
def loginFunc(request):
    if request.method == 'POST':
        user_name = request.POST['tname']
        user_password = request.POST['tpassword']
        myuser = authenticate(username=user_name, password=user_password)
        if myuser is not None:
            if myuser.is_superuser or myuser.is_staff:
                u1 = User.objects.get(username=user_name)
                request.session['myuser'] = u1.id  # based on the id we are getting a details
                request.session['myUserName'] = u1.username
                login(request,u1)
                return render(request, 'index.html', {'data': u1.username})
        else:
            return render(request, 'login.html', {'msg': 'Invalid credentials!!!'})
    return render(request,'login.html')

@never_cache
def registerFunc(request):
    if request.method == 'POST':
        uname = request.POST['tname']
        useremail = request.POST['tmail']
        userpswd = request.POST['tpassword']
        if User.objects.filter(username=uname).exists():
            return render(request, 'register.html', {'user_available': True})
        elif User.objects.filter(email=useremail).exists():
            return render(request, 'register.html', {'email_available': True})
        else:
            user = User.objects.create_user(email=useremail, password=userpswd, username=uname)
            user.save()
            return render(request, 'login.html')
    return render(request,'register.html')

@never_cache
def logoutFunc(request):
    logout(request)
    request.session['myuser'] = None  # based on the id we are getting a details
    request.session['myUserName'] = None
    return redirect(loginFunc)

@login_required
def search(request):
    value = request.GET['tbsearch']
    students = Student.objects.all()
    studentsList=[]
    for student in students:
        if student.Name == value or student.Course.CourseName==value or str(student.phoneNo) == value or student.Email == value or str(student.Age) == value:
            studentsList.append(student)
    if len(studentsList) != 0:
        return render(request,'searchResults.html',{'res':studentsList,'msg':'', 'count' : len(studentsList)})
    else:
        return render(request, 'searchResults.html', {'res': studentsList,'msg':'No results found....', 'count' : len(studentsList)})


