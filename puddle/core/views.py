from django.shortcuts import render, HttpResponse, redirect
from item.models import Category, Item
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
# Create your views here.


# show items on homepage
def index(request):
    items=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()
    return render(request, 'core/index.html', {
        'categories':categories,
        'items':items,
    })

# redirect to contact page
def contact(request):
    return render(request, "core/contact.html")


# create sign up view function to handle sign up form
def signup(request):
    if request.method=="POST":
       form=SignupForm(request.POST)
       

       # check if form is valid
       if form.is_valid():
           form.save()

           return redirect("/login/")
    else:
       form=SignupForm() 

    return render(request, "core/signup.html", {
        "form":form
    })


# create login view function to handle login form
def login_view(request):
    if request.method=="POST":
        form=LoginForm(request.POST) 

        # check if form is valid
        if form.is_valid():

            # authenticate user
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user =authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                form.add_error(None, "Invalid username or password")

            
    else:
        form=LoginForm()

    return render(request, "core/login.html", {
            "form":form
        })

# Logout
def logout_view(request):
    logout(request)
    return redirect("core:index")  # Redirect to homepage after logout