from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', include('Book.urls')),
    path('user/', include('User.urls')),
    path('search/', include('Search.urls')),
    path('chapter/', include('Chapter.urls')),
]
