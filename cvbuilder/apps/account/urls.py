from django.urls import path
from django.contrib.auth.views import LogoutView
from apps.account.views import (
    LoginView,
    SignUpView,
    UserProfile
)

app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfile.as_view(), name='profile'),

]
