from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.contrib.auth import login
from .forms import RegisterForm
from .models import CustomUser
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin


class UserView(LoginRequiredMixin, View):
    login_url = '/user/login/'

    def get(self, request):
        user = request.user
        # bought_book = CustomUser.objects.bought_book.split('@')
        # data = {'Books': Book.object.filter().order_by('-created_at')}
        return render(request, 'user.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
