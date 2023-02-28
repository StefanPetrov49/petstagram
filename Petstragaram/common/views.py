from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from Petstragaram.common.forms import CommentForm, SearchForm
from Petstragaram.common.models import PhotoLike
from Petstragaram.photos.models import Photo




def index(request):
    all_photos = Photo.objects.all()
    search_form = SearchForm()
    comment_form = CommentForm()
    user = request.user
    if request.user.is_anonymous:
        all_liked_photos_by_user = []
    else:
        all_liked_photos_by_user = [like.to_photo_id for like in user.photolike_set.all()]
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            all_photos = all_photos.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])

    context = {
        'photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form,
        'all_liked_photos_by_user': all_liked_photos_by_user,
    }
    return render(request, 'common/home-page.html', context)


def like_photo(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = PhotoLike.objects.filter(to_photo_id=photo_id, user=request.user).first()

    if liked_object:
        liked_object.delete()
    else:
        like = PhotoLike(to_photo=photo, user=request.user)
        like.save()

    redirect_path = request.META['HTTP_REFERER'] + f'#photo-{photo_id}'
    return redirect(redirect_path)


def share_photo(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('details photo', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#photo-{photo_id}')


def add_comment(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.filter(pk=photo_id).get()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.user = request.user
            comment.save()
        return redirect(request.META['HTTP_REFERER'] + f'#photo-{photo_id}')
