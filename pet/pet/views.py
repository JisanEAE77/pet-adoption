from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import  AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Pet

from .models import Pet,CustomUser
from .forms import PetForm

def index(request, *args, **kwargs):
    pets = Pet.objects.all()[:8]
    context = {
        'pets': pets,
    }
    return render(request, "index.html", context)

def register_view(request):
    errors = None
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            errors = form.errors.as_data()
            print(request.POST)  # Add this line to print form data
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form, 'errors': errors})

def login_view(request):
    errors = None
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            errors = form.errors.as_data()
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'errors': errors})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    
def singlepet(request, id):
    pet = Pet.objects.get(id=id)

    context = {
        'pet': pet,
    }

    return render(request, "singlepet.html", context)

def pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('/profile/self/')
    else:
        form = PetForm()
    return render(request, 'pet_create.html', {'form': form})

def pet_update(request, pk):
    pet = get_object_or_404(Pet, pk=pk, user=request.user)
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('/profile/self/')
    else:
        form = PetForm(instance=pet)
    return render(request, 'pet_update.html', {'form': form})

def pet_delete(request, pk):
    pet = get_object_or_404(Pet, pk=pk, user=request.user)
    if request.method == 'POST':
        pet.delete()
        return redirect('/profile/self/')
    return render(request, 'pet_delete.html', {'pet': pet})

def profile_view(request, username):
    user = get_object_or_404(CustomUser, username=username)
    pets = Pet.objects.filter(user=user)
    context = {
        'user': user,
        'pets': pets,
    }
    return render(request, 'profile.html', context)

@login_required
def self_profile_view(request):
    user = request.user
    pets = Pet.objects.filter(user=user)
    context = {
        'user': user,
        'pets': pets,
    }
    return render(request, 'self_profile.html', context)

def all_pets_view(request):
    all_pets = Pet.objects.order_by('-date_posted')
    context = {
        'all_pets': all_pets,
    }
    return render(request, 'all_pets.html', context)

def adopt(request, id):
    pet = Pet.objects.get(id=id)

    pet.adopted_by = request.user
    pet.is_adopted = True

    pet.save()

    return redirect('/myadoption')

def myadoptions(request, *args, **kwargs):
    all_pets = Pet.objects.filter(adopted_by=request.user.id)

    context = {
        "all_pets": all_pets,
    }

    return render(request, "myadoptions.html", context)