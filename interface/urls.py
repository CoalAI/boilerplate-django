from django.urls import path , include
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from . import views

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('accounts/', include('authemail.urls')),
    path('google-login/', views.GoogleLoginView.as_view(), name='google_login'),
    path('google-callback/', views.GoogleCallbackView.as_view(), name='google_callback'),
]
