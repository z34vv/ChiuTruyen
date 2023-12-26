from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.views import View
from User.models import CustomUser, Author
from Book.models import Category, Book, Chapter, Page, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from dateutil.relativedelta import relativedelta


def readChapter(request, book_id, chapter_number):
    user = request.user
    book = get_object_or_404(Book, id=book_id)
    chapter = get_object_or_404(Chapter, book=book, number=chapter_number)
    if user.id not in book.bought_user.split('@')[1:-1]:
        if user.id not in chapter.bought_user.split('@')[1:-1]:
            author = book.author.user
            if user.vip_end_duration is None:
                user.wallet -= 5000
                author.wallet += 5000
            else:
                user.wallet -= 4500
                author.wallet += 4500
            author.save()
            chapter.bought_user += str(user.id) + '@'
            user.save()
    pages = Page.object.filter(chapter__number=chapter_number).order_by('id')
    book.view += 1
    book.save()
    chapter.view += 1
    chapter.save()
    bought = True
    return render(request, 'readBook.html', {'book': book, 'chapter': chapter, 'pages': pages, 'bought': bought})
