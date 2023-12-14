from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.UserView.as_view(), name='user'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/user/login'), name='logout'),
    # path('repairName/', views.repairName, name='repairName'),
    # path('create_playlist', views.createPlaylist, name='create_playlist'),
    # path('create_playlist_form', views.createPlaylistView, name='create_playlist_form')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
