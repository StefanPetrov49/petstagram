from django.shortcuts import render, redirect

from Petstragaram.common.forms import CommentForm
from Petstragaram.photos.forms import PhotoCreateForm, PhotoEditForm
from Petstragaram.photos.models import Photo


def add_photo(request):
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            form.save_m2m()
            photo.save()

            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'photos/photo-add-page.html', context)


def details_photo(request, pk):
    comment_form = CommentForm()
    photo = Photo.objects.filter(pk=pk).get()
    likes = photo.photolike_set.all()
    photo_is_liked_by_user = likes.filter(user=request.user)
    comments = photo.photocomment_set.all()
    is_owner = request.user == photo.user

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'comment_form': comment_form,
        'photo_is_liked_by_user': photo_is_liked_by_user,
        'is_owner': is_owner,
    }
    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = PhotoEditForm(instance=photo)
    else:
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
        return redirect('details photo', pk=pk)

    context = {
        'form': form,
        'primary_key': pk,
    }

    return render(request, 'photos/photo-edit-page.html', context)

def delete_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    photo.delete()
    return redirect('index')