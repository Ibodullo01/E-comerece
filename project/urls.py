"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include     ('blog.urls'))
"""
import debug_toolbar
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

token_urlpatterns = [



]


urlpatterns = i18n_patterns(
    #token url
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # debug toolbar
    path('__debug__/', include(debug_toolbar.urls)),

    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('account/' , include('account.urls')),
    path('order/', include('order.urls')),
)

api_urls = [
    path('api/v0/account/', include('account.api.v0.urls')),
    path('api/v0/product/', include('product.api.v0.urls')),
    path('api/v0/order/', include('order.api.v0.urls')),
]

urlpatterns += api_urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)