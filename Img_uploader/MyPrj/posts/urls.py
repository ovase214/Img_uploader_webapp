from django.contrib import admin
from django.urls import path
from .views import HomePageView, CreatePostView,SignUpView,Home1View
from django.contrib.auth import views as auth_views
from .views import DeleteImg

urlpatterns = [
    
    path('', HomePageView.as_view(), name='home'),
    path('Img_list/', Home1View.as_view(), name='Img_list'),
    path('dashboard/', CreatePostView.as_view(), name='dashboard'),

    # Authentication 
    path('register/', SignUpView.as_view(), name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'),name='logout'),  
    path('Img_list/<pk>/Delete/', DeleteImg.as_view(),name='Delete'),
    ]


