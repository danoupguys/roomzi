from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render


def home_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'commons/index.html', {'signup': form})


# Create your views here.
def about_us(request):
    return render(request, 'commons/about-us.html')
