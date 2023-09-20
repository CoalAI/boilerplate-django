from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from authemail.views import (PasswordReset, PasswordResetVerified,
                              SignupVerify)

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('signup/verify/', SignupVerify.as_view(), name='signup-verify'),
    path('password/reset/', PasswordReset.as_view(), name='password-reset'),
    path('password/reset/verified/', PasswordResetVerified.as_view(), name='password-reset-verified'),
    path('social-auth/', RedirectView.as_view(url=reverse_lazy('social:begin', args=['google-oauth2'])), name='social-auth')
]
