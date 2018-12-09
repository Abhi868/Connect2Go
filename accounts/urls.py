
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path('',views.home, name="home"),
    path('register/' ,views.register, name="register"),
    path('profile/' ,views.profile, name="profile"),
    path('editprofile/' ,views.editprofile, name="editprofile"),
    path('change_password/',views.change_password,name="change_password"),
    path('reset-password/',auth_views.password_reset, {'template_name': 'accounts/reset_password.html'},name="password_reset"),
    path('reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+))' ,auth_views.password_reset_confirm,name="password_reset_confirm"),
    path('reset-password/complete/' ,auth_views.password_reset_complete,name="password_reset_complete"),
    path('reset-password/done' ,auth_views.password_reset_done,name="password_reset_done"),
    path('login/' ,auth_views.login, {'template_name': 'accounts/login.html'}, name="login"),
    path('logout/' ,auth_views.logout,{'template_name': 'accounts/logout.html'}, name="logout"),
]