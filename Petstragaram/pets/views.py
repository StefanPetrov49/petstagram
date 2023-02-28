from django.shortcuts import render, redirect

from Petstragaram.common.forms import CommentForm
from Petstragaram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from Petstragaram.pets.models import Pet


def details_pet(request, username, pet_name):
    comment_form = CommentForm()
    pet = Pet.objects.get(slug=pet_name)
    all_photos = pet.photo_set.all()
    context = {
        'pet': pet,
        'all_photos': all_photos,
        'comment_form': comment_form,
    }
    return render(request, 'pets/pet-details-page.html', context)


def add_pet(request):
    if request.method == "GET":
        form = PetCreateForm()
    else:
        form = PetCreateForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
        return redirect('details user', pk=1)

    context = {
        'form': form
    }
    return render(request, 'pets/pet-add-page.html', context)


def edit_pet(request, username, pet_name):
    pet = Pet.objects.filter(slug=pet_name).get()
    if request.method == "GET":
        form = PetEditForm(instance=pet)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
        return redirect('details pet', username=username, pk=1)

    context = {
        'form': form,
        'pet_name': pet_name,
        'username': username,
    }

    return render(request, 'pets/pet-edit-page.html', context)


def delete_pet(request, username, pet_name):
    pet = Pet.objects.filter(slug=pet_name).get()
    if request.method == "GET":
        form = PetDeleteForm(instance=pet)
    else:
        form = PetDeleteForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
        return redirect('details user', pk=1)

    context = {
        'form': form,
        'pet_name': pet_name,
        'username': username,
    }
    return render(request, 'pets/pet-delete-page.html', context)
