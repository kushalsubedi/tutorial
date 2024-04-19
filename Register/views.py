from django.shortcuts import render

# Create your views here.
from .forms import UserRegisterForm
from django.contrib import messages
def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            print(username)
            form.save()
            print ("HEllo world")
            messages.success(request, f'Account created for {username}')
        else:
            print (form.errors)
    else:
        form = UserRegisterForm()
    return render(request, 'Register/register.html', {'form': form})