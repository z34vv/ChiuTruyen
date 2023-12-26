from django.contrib import admin
from .models import CustomUser, Author
from Book.models import Book
# Register your models here.


class CustomUserAmin(admin.ModelAdmin):
    list_display = [
        'username',
        'email',
        'wallet',
        'created_at'
    ]


class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'stage_name',
        'number_of_book'
    ]


admin.site.register(CustomUser, CustomUserAmin)
admin.site.register(Author, AuthorAdmin)
