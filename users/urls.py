from django.urls import path
from django.contrib.auth.views import LoginView
from users.views import UserClickCountListView
app_name = "users"
urlpatterns = [
    path('login/', 
        LoginView.as_view(
            template_name='users/login.html'
        ), 
        name="login"
    ),
        path('click-counts/', UserClickCountListView.as_view(), name='click_counts'),

]