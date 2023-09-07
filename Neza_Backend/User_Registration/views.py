from django.shortcuts import render
from .forms import UserUploadForm
from User_Registration.models import User

def register_user(request):                   
    if request.method == 'POST':
        form = UserUploadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserUploadForm()

    return render(request, 'User_Registration/register.html', {'form':form})
    
