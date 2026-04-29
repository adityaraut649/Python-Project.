from django.urls import path, include   # 👈 include import
from . import views

urlpatterns = [
    path('', views.say_hello , name="say_hello"),   
    path('Open_signup', views.Open_signup , name = "Open_signup" ),
    path('Open_signin', views.Open_signin , name = "Open_signin" ),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin")
]