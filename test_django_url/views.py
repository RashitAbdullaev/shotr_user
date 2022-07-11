from django.contrib.auth.views import LoginView, LogoutView
from .forms import AuthUserForm, RegisterUserForm, CreateUrlForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import *
import pyshorteners
import json
from rest_framework import generics
from rest_framework.response import Response
from .serializers import ShortUrlSerializer


class UrlView(ListView):
    template_name = 'test_django_url/short_url.html'
    model = ShortUrl

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['short_url'] = ShortUrl.objects.all()
        return context


class CreateUrl(CreateView):
    template_name = 'test_django_url/create_url.html'
    form_class = CreateUrlForm
    success_url = reverse_lazy('short_url')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class MyProjectLoginView(LoginView):
    template_name = 'test_django_url/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('short_url')

    def get_success_url(self):
        return self.success_url


class RegisterUserView(CreateView):
    model = User
    template_name = 'test_django_url/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('short_url')


class MyUserLogout(LogoutView):
    next_page = reverse_lazy('short_url')


class AddJsonApi(generics.ListCreateAPIView):
    queryset = ShortUrl.objects.all()
    serializer_class = ShortUrlSerializer

    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body)
        s = pyshorteners.Shortener()
        url_short = s.tinyurl.short(data['url'])
        data = {
            'url': url_short,
        }
        return Response(data)
