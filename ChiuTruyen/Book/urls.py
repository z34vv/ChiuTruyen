from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:id>/', views.filterByCategory, name=''),
    path('buy-book/<int:id>/', views.buyBook, name='buy-book'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
