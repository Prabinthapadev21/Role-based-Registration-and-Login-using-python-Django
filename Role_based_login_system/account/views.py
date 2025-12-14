from django.shortcuts import render,redirect
from .forms import SignupForm,LoginForm
from django.contrib.auth import authenticate,login
# Create your views here.
def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)

                if user.role == 'admin':
                    return redirect('admin')
                elif user.role == 'employee':
                    return redirect('employee')
                elif user.role == 'customer':
                    return redirect('customer')
            else:
                msg = "Invalid credentials"
        else:
            msg = "error validating form"
    return render(request,'accounts/login.html',{'form':form,'msg':msg})

def register_view(request):
    msg = None
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = "user created successfully"
            return redirect('login')
        else:
            msg = "form is not valid"
    else:
        form = SignupForm()
    return render(request,'accounts/registration.html',{'form':form,'msg':msg})

def logout_view(request):
    return redirect('login')

def admin_page(request):
    return render(request,'roles/admin_page.html')

def employee_page(request):
    return render(request,'roles/employee_page.html')

def customer_page(request):
    return render(request,'roles/customer_page.html')