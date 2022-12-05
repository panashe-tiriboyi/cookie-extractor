from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer




'''@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegitrationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            accounts = serializer.save()
            data['response'] = 'successfully registered a new user.'
            data['email'] = accounts.email
            data['username'] = accounts.username
        else:
            data = serializer.errors
        return Response(data)'''