# notes_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from notes.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]
