from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('book/<int:id>/', views.bookDetailView, name='book'),
    path('<int:id>/', views.filterByCategory, name='search-buy-category'),
    path('buy-book/', views.buyBook, name='buy-book'),
    path('buy-vip/', views.buyVip, name='buy-vip'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
