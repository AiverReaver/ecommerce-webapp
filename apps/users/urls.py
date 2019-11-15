from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .jwttoken import MyTokenObtainPairView
from .views import register_customer, register_seller

urlpatterns = [
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/customer/", register_customer),
    path("register/seller/", register_seller),
]
