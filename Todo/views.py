from django.shortcuts import render,redirect
from .forms import RegisterForm,ContactForm
from .models import Contact
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    context = {}
    return render(request,'index.html')


def home(request):
    return render(request,'todo.html')




def com(request):
    form = ContactForm()
    # retrieve all Contact
    cox = Contact.objects.all()
    form = ContactForm()
    if request.method =='POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print('post happened')
            # grab the data and save
            print(request.POST['firstname'])
            print(form.cleaned_data.get('firstname'))

            form.save()
            return redirect('logout')

        else:
            form = ContactForm()    
    context  = {
        'form':form,
        'contacts':cox,
    }       
 

   
    return render(request,'contact.html',context)


    # register

def registerpage(request):
    form = RegisterForm()
    if request.method == 'POST':
      form = RegisterForm(request.POST)
      if form.is_valid():
          form.save()
          return redirect ('login') 
    context = { 
        'form': form
    }

    return render(request,'register.html',context)


# security

@login_required(login_url='login')
def todos(request):
    return render(request,'todo.html')


def loginpage(request):
  if request.user.is_authenticated:
    return redirect('todos')
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    theuser = authenticate(request,username=username,password=password)
    if theuser:
      login(request,theuser)
      return redirect('todos')
    else:
        messages.info(request,'Invalid Credentials')
  return render(request,'login.html')   
  


def logoutpage(request):
    logout(request)
    return redirect('index')

   