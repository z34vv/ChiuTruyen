from django.contrib import admin
from .models import Category, Book, Chapter, Page, Comment
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'created_at'
    ]


class BookAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'author',
        'display_categories',
        'status',
        'price',
        'created_at'
    ]

    def display_categories(self, obj):
        return ', '.join([category.name for category in obj.categories.all()])
    display_categories.short_description = 'Categories'


class ChapterAmin(admin.ModelAdmin):
    list_display = [
        'book',
        'name',
        'created_at'
    ]


class PageAdmin(admin.ModelAdmin):
    list_display = [
        'chapter'
    ]


class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'chapter',
        'created_at'
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Chapter, ChapterAmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Comment, CommentAdmin)
