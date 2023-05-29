from django.contrib.auth.forms import UserCreationForm 

class UserCreationForm(UserCreationForm):
    email = forms.EmailField()