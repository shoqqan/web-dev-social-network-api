from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def post_list(request):
    """
    List all posts or create a new post.

    GET:
    - Returns a list of all posts
    - No authentication required
    - Available to all users

    POST:
    - Creates a new post
    - Requires authentication
    - The authenticated user will be set as the author

    Request Body (POST):
    - title: string (required) - The title of the post
    - content: string (required) - The content of the post

    Responses:
    - 200: Successful retrieval of posts list (GET)
    - 201: Post successfully created (POST)
    - 400: Invalid data provided (POST)
    - 401: Authentication credentials not provided (POST)
    """
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Check if user is authenticated
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # Set the author to the authenticated user
        request.data['author'] = request.user.id
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    """
    Retrieve, update or delete a specific post.

    GET:
    - Returns details of a specific post
    - No authentication required
    - Available to all users

    PUT:
    - Updates an existing post
    - Requires authentication
    - User can only update their own posts
    - The authenticated user must be the author of the post

    DELETE:
    - Deletes an existing post
    - Requires authentication
    - User can only delete their own posts
    - The authenticated user must be the author of the post

    Parameters:
    - pk: integer (required) - The unique identifier of the post

    Request Body (PUT):
    - title: string (required) - The updated title of the post
    - content: string (required) - The updated content of the post

    Responses:
    - 200: Successful retrieval (GET) or update (PUT) of post
    - 204: Post successfully deleted (DELETE)
    - 400: Invalid data provided (PUT)
    - 401: Authentication credentials not provided (PUT, DELETE)
    - 403: User is not the author of the post (PUT, DELETE)
    - 404: Post not found
    """
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Check if user is authenticated
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # Ensure the user can only update their own posts
        if post.author.id != request.user.id:
            return Response(
                {"detail": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN
            )

        request.data['author'] = request.user.id
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Check if user is authenticated
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # Ensure the user can only delete their own posts
        if post.author.id != request.user.id:
            return Response(
                {"detail": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN
            )

        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
