from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import signForm
from tablib import Dataset
from .resources import Na_Reading
# from .forms import UserRegisterForm


# Create your views here.

def sign_create_view(request):
    form1 = signForm(request.POST)
    if form1.is_valid():
        form1.save()
        return redirect('login')
    else:
        form1 = signForm()
#    context = {'form' : form}
    return render(request,"user/sign_create.html", {'form1':form1})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You can Log In now')
            return redirect('sign')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form':form})


def csvupload(request):
    if request.method == 'POST':
        read_source = Na_Reading()
        dataset = tablib.Dataset(headers = ['intensity','na_level'])
        new_level = request.FILES['reading']

        imported_data = dataset.load(new_level.read())
        result = read_source.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            read_source.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'user/import.html')
