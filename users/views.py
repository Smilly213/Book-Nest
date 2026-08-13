from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView, DetailView

from .forms import ProfileForm
from .models import Profile

class AddProfile(FormView):
    form_class = ProfileForm
    template_name = 'users/addprofile.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DetailProfile(DetailView):
    model = Profile
    template_name = 'users/profile.html'
    context_object_name = 'profile'
    slug_url_kwarg = 'profile_slug'

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, slug=self.kwargs[self.slug_url_kwarg])
