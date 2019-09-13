from django.urls import path,include
from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('startquiz/', views.start_quiz, name='startquiz'),
    path('signup/', views.signup,name='signup'),
    path('startquiz/<int:question_id>', views.startquiz, name='startquiz'),
]