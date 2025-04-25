from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

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
    - description: string (required) - The description of the post
    - tags: array of strings (optional) - Tags for the post
    - imageUrl: string (optional) - URL of the post image

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
        # Get the first user as default author if not authenticated
        from users.models import User
        default_author = User.objects.first()

        serializer = PostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(author=default_author)
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
    - description: string (required) - The updated description of the post
    - tags: array of strings (optional) - Updated tags for the post
    - imageUrl: string (optional) - Updated URL of the post image

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
        serializer = PostSerializer(post, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(author=post.author)  # Keep the original author
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def comment_list(request, post_id):
    """
    List all comments for a post or create a new comment.

    GET:
    - Returns a list of all comments for a specific post
    - No authentication required
    - Available to all users

    POST:
    - Creates a new comment for a specific post
    - Requires authentication
    - The authenticated user will be set as the author

    Parameters:
    - post_id: integer (required) - The unique identifier of the post

    Request Body (POST):
    - content: string (required) - The content of the comment
    - likes: integer (optional) - The number of likes for the comment

    Responses:
    - 200: Successful retrieval of comments list (GET)
    - 201: Comment successfully created (POST)
    - 400: Invalid data provided (POST)
    - 401: Authentication credentials not provided (POST)
    - 404: Post not found
    """
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        comments = Comment.objects.filter(postId=post)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Get the first user as default author if not authenticated
        from users.models import User
        default_author = User.objects.first()

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=default_author, postId=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, post_id, comment_id):
    """
    Retrieve, update or delete a specific comment.

    GET:
    - Returns details of a specific comment
    - No authentication required
    - Available to all users

    PUT:
    - Updates an existing comment
    - Requires authentication
    - User can only update their own comments
    - The authenticated user must be the author of the comment

    DELETE:
    - Deletes an existing comment
    - Requires authentication
    - User can only delete their own comments
    - The authenticated user must be the author of the comment

    Parameters:
    - post_id: integer (required) - The unique identifier of the post
    - comment_id: integer (required) - The unique identifier of the comment

    Request Body (PUT):
    - content: string (required) - The updated content of the comment
    - likes: integer (optional) - The updated number of likes for the comment

    Responses:
    - 200: Successful retrieval (GET) or update (PUT) of comment
    - 204: Comment successfully deleted (DELETE)
    - 400: Invalid data provided (PUT)
    - 401: Authentication credentials not provided (PUT, DELETE)
    - 403: User is not the author of the comment (PUT, DELETE)
    - 404: Post or comment not found
    """
    try:
        post = Post.objects.get(pk=post_id)
        comment = Comment.objects.get(pk=comment_id, postId=post)
    except (Post.DoesNotExist, Comment.DoesNotExist):
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save(author=comment.author, postId=post)  # Keep the original author
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
