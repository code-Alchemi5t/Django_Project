from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import View

from user.forms import SignUpForm

class SignUp(View):
    def post(self,request):
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('home:all')
            else:
                ctx = {'form': form}
                return render(request, 'user/signup.html', ctx)
    def get(self,request):
        form = SignUpForm()
        return render(request, 'user/signup.html', {'form': form})

