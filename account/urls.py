from .views import login_view, logout_view , register ,profile
from django.urls import path

app_name = 'account'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('info/', profile, name='profile'),

]
