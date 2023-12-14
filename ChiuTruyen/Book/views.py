from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.views import View
from User.models import CustomUser, Author
from .models import Category, Book, Chapter, Pages, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
# from User.views import UserView


class HomeView(LoginRequiredMixin, View):
    login_url = '/user/login/'

    def get(self, request):
        data = {'Books': Book.object.all().order_by('-created_at')}
        return render(request, 'index.html', data)


def filterByCategory(request, id):
    category = Category.object.get(id=id)
    data = {'Books': Book.object.filter(category=category).order_by('-created_at')}
    return render(request, 'index.html', data)


def buyBook(request, id):
    user = request.user
    user.bought_book += str(id) + '@'
    return redirect(request.META.get('HTTP_REFERER'))
