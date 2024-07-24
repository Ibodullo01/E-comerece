from django.urls import path

from product import views
from .views import get_categories , product_detail , store

app_name = 'product'

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>', product_detail, name='detail'),
    path('category/<int:pk>', get_categories, name='get_categories'),
    path('store/', store, name='store'),

]

