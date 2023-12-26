from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.contrib.auth import login
from .forms import RegisterForm
from .models import CustomUser
from Book.models import Book
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin


class UserView(LoginRequiredMixin, View):
    login_url = '/user/login/'

    def get(self, request):
        user = request.user
        bought_book_ids = user.bought_book.split('@')[1:-1]
        bought_book_list = []
        for id in bought_book_ids:
            bought_book_list.append(Book.object.get(id=int(id)))
        bought_book_list = sorted(bought_book_list, key=lambda x: x.name)
        data = {'BoughtBooks': bought_book_list}
        return render(request, 'user.html', data)


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
