from django.shortcuts import render, redirect, HttpResponse
from blog.models import Post
from courses.models import Course, Tutorial
from .models import Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.messages import add_message, SUCCESS, ERROR

# Create your views here.


def main(request):
    allPosts = Post.objects.order_by("-timestamp")
    print(allPosts[:2])

    allCourses = Course.objects.order_by('-id')
    print(allCourses[:3])

    allSlugs = []

    for i in allCourses[:3]:
        tut = Tutorial.objects.filter(course=i.name).first()
        print(tut.slug)
        allSlugs.append(tut.slug)

    params = {"posts": allPosts[:2], "courses": zip(allCourses[:3], allSlugs)}

    return render(request, "home/index.html", params)


def about(request):
    return render(request, "home/about.html")


def contact(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('ph')
        concern= request.POST.get('concern')

        myContact = Contact(name=name, email=email, phone=phone, concern=concern)
        myContact.save()
        add_message(request, SUCCESS, "We have recieved your message!")
    return render(request, "home/contact.html")


def handleLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        myUser = authenticate(username=username, password=password)

        if myUser:
            add_message(request, SUCCESS, "You have logged in succesfully")
            login(request, myUser)
            return redirect('/')
        else:
            add_message(
                request, ERROR, "User doesn't exist. Check your credentials or create an account!")
            return redirect('/')
    return render(request, "home/login.html")


def handleLogout(request):
    logout(request=request)
    add_message(request, SUCCESS, "You have logged out succesfully")
    return redirect('/')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confPass']

        # Creating Checks
        if len(username) <= 10 and len(password) >= 8 and password == confirm_password:
            # Create the user
            try:
                myUser = User.objects.create_user(username, email, password)

                myUser.save()
                add_message(request, SUCCESS,
                            "Your iCoder has been successfully created!")
                redirect('/')

            except Exception as e:
                add_message(request, ERROR, "User Already Exists!")

        else:
            add_message(request, ERROR, "User Cannot be Created! Check :\nLength of "
                        "FirstName and LastName cannot be greater than 10 OR Both "
                        "the passwords must be same")
            redirect('/')

        return redirect('/')

    return render(request, "home/signup.html")

