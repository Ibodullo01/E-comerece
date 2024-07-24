from django.urls import path
from .views import SignUp,UserUpdate
app_name = 'api_account'

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('update_profile/<int:pk>', UserUpdate.as_view(), name='update_profile'),

]