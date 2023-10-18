from django.urls import path , include
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from django.urls import reverse_lazy
from django.views.generic import RedirectView
<<<<<<< HEAD
from authemail.views import Signup
=======
from .views import UserProfileUpdateView
>>>>>>> 89e2416672fea0af1b4e7804ce060017d77ce77f

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
<<<<<<< HEAD
    path('signup/', Signup.as_view(), name="signup"),
    path('social-auth/', RedirectView.as_view(url=reverse_lazy('social:begin', args=['google-oauth2'])), name='social-auth')
=======
    path('accounts/', include('authemail.urls')),
    path('social-auth/', RedirectView.as_view(url=reverse_lazy('social:begin', args=['google-oauth2'])), name='social-auth'),
    path('update-profile/', UserProfileUpdateView.as_view())
>>>>>>> 89e2416672fea0af1b4e7804ce060017d77ce77f
]
