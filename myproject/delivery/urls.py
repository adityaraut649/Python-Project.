from django.urls import path, include   # 👈 include import
from . import views

urlpatterns = [
    path('', views.say_hello , name="say_hello"),   
    path('Open_signup', views.Open_signup , name = "Open_signup" ),
    path('Open_signin', views.Open_signin , name = "Open_signin" ),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('open_add_restaurant', views.open_add_restaurant, name="open_add_restaurant"),
    path('add_restaurant', views.add_restaurant, name="add_restaurant"),
    path('open_show_restaurant', views.open_show_restaurant, name="show_restaurant"),
    path('open_update_restaurant/<int:restaurant_id>', views.open_update_restaurant, name="open_update_restaurant"),
    path('update_restaurant/<int:restaurant_id>', views.update_restaurant, name='update_restaurant'), 
    path('delete_restaurant/<int:restaurant_id>', views.delete_restaurant, name="delete_restaurant"),
    path('open_update_menu/<int:restaurant_id>', views.open_update_menu, name='open_update_menu'), 
    path('update_menu/<int:restaurant_id>', views.update_menu, name='update_menu'),
    path('view_menu/<int:restaurant_id>/<str:username>', views.view_menu, name='view_menu'), 
]