from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def users(request):
    """
    List all users in the system or create a new user.

    GET: Returns a list of all users with their details.
    POST: Creates a new user with the provided data.

    * Requires no authentication
    * Available to all users
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
