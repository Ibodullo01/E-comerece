from django.urls import path
from .views import (CategoryListApiView, ProductListApiView, ProductByCategoryApiView, ProductDetailSerializer,
                    ProductDetailApiView , CommentCreateApiView , CommentByProductApiView)

app_name = 'api_product'

urlpatterns = [
    path('categories/', CategoryListApiView.as_view(), name='category-list'),
    path('products/', ProductListApiView.as_view(), name='product-list'),
    path('category/<int:pk>', ProductByCategoryApiView.as_view(), name='product-by-category'),
    path('detail/<int:pk>' , ProductDetailApiView.as_view(), name='product-detail' ),
    path('comment-create/' , CommentCreateApiView.as_view(), name='comment-create'),
    path('comment-by-product/<int:pk>' , CommentByProductApiView.as_view(), name='comment-by-product'),
]