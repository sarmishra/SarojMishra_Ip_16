from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate

def home(request):
	template_name='login/home.html'
	return render(request,template_name)

def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('login')

    else:
        form=UserCreationForm()

    return render(request,'signup.html',{'form':form})



@login_required
def dashboard(request):
	template_name='login/dashboard.html'
	return render(request,template_name)
	
