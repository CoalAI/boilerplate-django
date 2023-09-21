from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from .models import MyUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import HttpResponseRedirect
from urllib.parse import urlencode

class GoogleLoginView(APIView):
    def get(self, request):

        auth_url = (
            f'https://accounts.google.com/o/oauth2/auth?'
            f'client_id={settings.GOOGLE_OAUTH2_CLIENT_ID}&'
            f'redirect_uri={settings.GOOGLE_OAUTH2_REDIRECT_URI}&'
            f'response_type=code&'
            f'scope=openid%20email%20profile&'
            f'prompt=select_account'
        )

        return Response({'auth_url': auth_url}, status=status.HTTP_200_OK)
    

class GoogleCallbackView(APIView):
    def get(self, request):
        code = request.query_params.get('code')
        if not code:
            return Response({'detail': 'Missing code parameter'}, status=status.HTTP_400_BAD_REQUEST)

        token_url = 'https://accounts.google.com/o/oauth2/token'
        token_data = {
            'code': code,
            'client_id': settings.GOOGLE_OAUTH2_CLIENT_ID,
            'client_secret': settings.GOOGLE_OAUTH2_CLIENT_SECRET,
            'redirect_uri': settings.GOOGLE_OAUTH2_REDIRECT_URI,
            'grant_type': 'authorization_code',
        }

        response = requests.post(token_url, data=token_data)
        token_info = response.json()

        if 'access_token' in token_info:
            user_info_url = 'https://www.googleapis.com/oauth2/v2/userinfo'
            headers = {'Authorization': f'Bearer {token_info["access_token"]}'}
            user_info_response = requests.get(user_info_url, headers=headers)
            user_info = user_info_response.json()
            email = user_info.get('email')
            first_name = user_info.get('given_name')
            last_name = user_info.get('family_name')
            if email:
                user, created = MyUser.objects.get_or_create(email=email)
                if created:
                    user.is_verified = True
                    if first_name:
                        user.first_name = first_name
                    if last_name:
                        user.last_name = last_name

                    user.save()

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            query_parameters = {
                'access_token': access_token,
                'refresh_token': str(refresh),
            }
            auth_url = settings.FRONTEND_REDIRECT_URL

            redirect_url = f'{auth_url}?{urlencode(query_parameters)}'

            return HttpResponseRedirect(redirect_url)
        return Response({'detail': 'Authentication failed'}, status=status.HTTP_400_BAD_REQUEST)
