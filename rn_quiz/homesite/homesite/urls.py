
from django.contrib import admin
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from quiz import forms, views
from datetime import datetime

urlpatterns = [
    path('', include('quiz.urls')),
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/',
         LoginView.as_view
         (
             template_name='login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('quiz/', include('quiz.urls')),
]
