from django.urls import path , include
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from django.urls import reverse_lazy
from django.views.generic import RedirectView

app_name = 'interface'
urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('accounts/', include('authemail.urls')),
    path('social-auth/', RedirectView.as_view(url=reverse_lazy('social:begin', args=['google-oauth2'])), name='social-auth')
]
