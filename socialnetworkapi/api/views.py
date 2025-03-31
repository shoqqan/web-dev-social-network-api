from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .models import Post
from .serializer import UserSerializer
from .serializer import PostSerializer

@api_view(['GET'])
def get_user(request):
    return Response(UserSerializer({'name':''}))

