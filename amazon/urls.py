from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.signin_user),
    path('signin', views.signin_user),
    path('signup', views.signup_user),
    path('logout', views.logoutuser),
    path('home', views.home)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
