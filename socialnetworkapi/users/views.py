from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

# Create your views here.

@api_view(['GET'])
def users(request):
    """
    List all users in the system.

    Returns a list of all users with their details.

    * Requires no authentication
    * Available to all users
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def user_detail(request, id=None):
    """
    Retrieve details of a specific user.

    Returns detailed information about a user identified by the ID.

    * Requires no authentication
    * Available to all users

    Parameters:
    - id: The unique identifier of the user

    Responses:
    - 200: Successful retrieval of user details
    - 404: User not found
    """
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
