from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
]
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:id>/', views.movie_detail, name='movie_detail'),


    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    ]

