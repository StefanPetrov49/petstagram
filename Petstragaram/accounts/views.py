from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from Petstragaram.accounts.forms import AppUserCreateForm

UserModel = get_user_model()


class UserLoginView(LoginView):
    template_name = 'accounts/login-page.html'


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')


class UserRegisterView(CreateView):
    form_class = AppUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        login(request, self.object)
        return response


class UserDeleteView(DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')


class UserDetailsView(DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'
    photos_paginate_by = 2

    def get_photos_page(self):
        return self.request.GET.get('page', 1)

    def get_paginated_photos(self):
        page = self.get_photos_page()

        photos = self.object.photo_set \
            .order_by('-date_of_publication')

        paginator = Paginator(photos, self.photos_paginate_by)
        return paginator.get_page(page)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        context['pets_count'] = self.object.pet_set.count()

        photos = self.object.photo_set \
            .prefetch_related('photolike_set')

        context['photos_count'] = photos.count()
        context['likes_count'] = sum(x.photolike_set.count() for x in photos)

        context['photos'] = self.get_paginated_photos()
        context['pets'] = self.object.pet_set.all()

        return context


class UserEditView(UpdateView):
    model = UserModel
    fields = ('first_name', 'last_name', 'gender', 'email', 'profile_picture')
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.object.pk
        })
