from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserProfileUpdateSerializer, UserProfileRetrieveSerializer

class UserProfileUpdateView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserProfileRetrieveSerializer
        else:
            return UserProfileUpdateSerializer

    def get_object(self):
        return self.request.user