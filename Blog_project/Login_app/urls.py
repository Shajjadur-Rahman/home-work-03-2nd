from django.urls import path
from . import views

app_name = 'Login_app'

urlpatterns = [
    path('signup/', views.sign_up_user, name='signUp'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.log_out_user, name='logout'),
    path('profile/', views.user_profile, name='user_profile'),
    path('edit-profile/', views.edit_user_profile, name='edit_user_profile'),
    path('change-pro-pic/', views.change_pro_pic, name='change_pro_pic'),
]