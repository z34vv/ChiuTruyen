from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.views import View
from User.models import CustomUser, Author
from .models import Category, Book, Chapter, Page, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from dateutil.relativedelta import relativedelta
# from User.views import UserView


class HomeView(LoginRequiredMixin, View):
    login_url = '/user/login/'

    def get(self, request):
        data = {'Books': Book.object.all().order_by('-created_at')}
        return render(request, 'index.html', data)


def bookDetailView(request, id):
    book = Book.object.get(id=id)
    categories = book.categories.all()
    chapters = Chapter.object.filter(book=book).order_by('name')
    return render(request, 'bookDetail.html', {'book': book, 'categories': categories, 'chapters': chapters})


def filterByCategory(request, id):
    category = Category.object.get(id=id)
    data = {'Books': Book.object.filter(category=category).order_by('-created_at')}
    return render(request, 'index.html', data)


def buyBook(request):
    user = request.user
    bought_book_list = user.bought_book.split('@')[1:-1]
    book_id = request.POST.get('id')
    this_book = Book.object.get(pk=book_id)
    if book_id not in bought_book_list:
        if user.wallet >= this_book.price:
            user.bought_book += str(book_id) + '@'
            this_book.bought_user += str(user.id) + '@'
            this_book.save()

            author = this_book.author.user
            if user.vip_end_duration is None:
                price = this_book.price
            else:
                price = this_book.price * 90 / 100
            author.wallet += price
            author.save()
            user.wallet -= price
            user.save()
        else:
            print('Số dư của quý khách không đủ! Vui lòng nạp thêm để tiếp tục')
    else:
        print('Bạn đã mua cuốn này rồi!')
    return redirect(request.META.get('HTTP_REFERER'))


def buyVip(request):
    user = request.user
    months = int(request.POST.get('months'))
    if months == 1:
        if user.wallet >= 49000:
            updateVip(user, 1)
            user.wallet -= 49000
            print('True')
    elif months == 3:
        if user.wallet >= 149000:
            updateVip(user, 3)
            user.wallet -= 149000
    elif months == 6:
        if user.wallet >= 299000:
            updateVip(user, 6)
            user.wallet -= 299000
    elif months == 12:
        if user.wallet >= 499000:
            updateVip(user, 12)
            user.wallet -= 499000
    else:
        print('Số dư của quý khách không đủ! Vui lòng nạp thêm để tiếp tục')
    user.save()
    return redirect(request.META.get('HTTP_REFERER'))


def updateVip(user, months):
    if user.vip_end_duration is None:
        user.vip_end_duration = timezone.now() + relativedelta(months=months)
    else:
        user.vip_end_duration += relativedelta(months=months)

    if user.vip_end_duration.month > 12:
        user.vip_end_duration += relativedelta(years=1)
        user.vip_end_duration -= relativedelta(months=12)
    if user.vip_end_duration.month == 2 and user.vip_end_duration.day > 28:
        user.vip_end_duration += relativedelta(months=1)
        user.vip_end_duration -= relativedelta(days=28)
    user.save()
