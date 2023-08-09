from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, CreateRecordForm
from .models import Record

def home(request):
    if request.user.is_authenticated:
        records = Record.objects.all()
        # check to see if person is logging in
        return render(request, 'home.html', {'records':records})
    else:
        messages.warning(request, message=f"User must log in first!")
        return redirect('login')

# def lookup(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         #Authenticate
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, message=f"You have been logged in")
#             return redirect('home')
#         else:
#             messages.error(request, message=f"Invalid Credentials! There was an error logging in, Please try again...")
#             return redirect('login')
#     else:
#         return render(request, 'lookup.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, message=f"You have been logged in")
            return redirect('home')
        else:
            messages.error(request, message=f"Invalid Credentials! There was an error logging in, Please try again...")
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.warning(request, message=f"You have been Logged Out...")
    return redirect('login')

# def register_user(request):
#     return render(request, 'register.html', {})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, message=f'Account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', { 'form': form })

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.warning(request, message=f"User must log in first!")
        return redirect('login')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        record = get_object_or_404(Record, pk=pk)
        if request.user == record.author:
            delete_it = Record.objects.get(id=pk)
            delete_it.delete()
            messages.warning(request, message=f"Record Deleted Successfully.")
            return redirect('home')
        else:
            messages.warning(request, message=f"User have no rights to do so!")
            return redirect('record', pk=pk)
    else:
        messages.warning(request, message=f"User must log in first!")
        return redirect('login')

def create_record(request):
    if request.user.is_authenticated:
        title = 'Create Record'
        submit_button = 'Create'
        if request.method == 'POST':
            form = CreateRecordForm(request.POST)
            if form.is_valid():
                form.save()
                messages.warning(request, message=f"Record Created Successfully.")
                return redirect('home')
        else:
            form = CreateRecordForm()
            return render(request, 'create_record.html', {'form':form, 'title':title, 'submit_button' : submit_button})
        
    else:
        messages.warning(request, message=f"User must log in first!")
        return redirect('login')

@login_required
def update_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    title = 'Update Record'
    submit_button = 'Update'

    if request.user == record.author:
        if request.method == 'POST':
            form = CreateRecordForm(request.POST, instance=record)
            if form.is_valid():
                form.save()
                return redirect('record', pk=pk)  # Redirect to a view displaying the updated record
        else:
            form = CreateRecordForm(instance=record)
            return render(request, 'create_record.html', {'form': form, 'title': title, 'submit_button' : submit_button})
    else:
        return redirect('home')

