from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("home")
        else:
            form = UserCreationForm()
            
        return render(request, "users/register.html", {"form": form})