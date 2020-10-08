
from rest_framework import viewsets

from api.models import User
from api.serializers import UserSerializer

"""
Using the model viewset for the view from the rest_framework
"""
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer