# Social Network API

This is a Django-based REST API for a social network application.

## API Documentation

### Authentication

No authentication is required for any endpoint in this API. All endpoints are publicly accessible.

### API Endpoints

#### Users

##### List Users
- **URL**: `/api/users/`
- **Method**: GET
- **Authentication Required**: No
- **Description**: Returns a list of all users in the system.
- **Response**: 200 OK
  ```json
  [
    {
      "id": "1",
      "username": "user1",
      "email": "user1@example.com",
      "first_name": "John",
      "last_name": "Doe"
    },
    {
      "id": "2",
      "username": "user2",
      "email": "user2@example.com",
      "first_name": "Jane",
      "last_name": "Smith"
    }
  ]
  ```

##### Get User Details
- **URL**: `/api/users/{id}/`
- **Method**: GET
- **Authentication Required**: No
- **Description**: Returns detailed information about a specific user.
- **Parameters**:
  - `id` (path parameter): The unique identifier of the user.
- **Response**: 200 OK
  ```json
  {
    "id": "1",
    "username": "user1",
    "email": "user1@example.com",
    "first_name": "John",
    "last_name": "Doe"
  }
  ```
- **Error Responses**:
  - 404 Not Found: User with the specified ID does not exist.

#### Posts

##### List Posts
- **URL**: `/api/posts/`
- **Method**: GET
- **Authentication Required**: No
- **Description**: Returns a list of all posts.
- **Response**: 200 OK
  ```json
  [
    {
      "id": 1,
      "title": "First Post",
      "description": "This is my first post",
      "author": "user1",
      "date": "2023-01-01T12:00:00Z",
      "tags": ["tag1", "tag2"],
      "imageUrl": "https://example.com/image.jpg"
    },
    {
      "id": 2,
      "title": "Second Post",
      "description": "This is another post",
      "author": "user2",
      "date": "2023-01-02T12:00:00Z",
      "tags": ["tag3"],
      "imageUrl": null
    }
  ]
  ```

##### Create Post
- **URL**: `/api/posts/`
- **Method**: POST
- **Authentication Required**: No
- **Description**: Creates a new post. The first user in the system will be set as the author.
- **Request Body**:
  ```json
  {
    "title": "New Post",
    "description": "This is a new post",
    "tags": ["tag1", "tag2"],
    "imageUrl": "https://example.com/image.jpg"
  }
  ```
- **Response**: 201 Created
  ```json
  {
    "id": 3,
    "title": "New Post",
    "description": "This is a new post",
    "author": "authenticated_user",
    "date": "2023-01-03T12:00:00Z",
    "tags": ["tag1", "tag2"],
    "imageUrl": "https://example.com/image.jpg"
  }
  ```
- **Error Responses**:
  - 400 Bad Request: Invalid data provided.

##### Get Post Details
- **URL**: `/api/posts/{pk}/`
- **Method**: GET
- **Authentication Required**: No
- **Description**: Returns detailed information about a specific post.
- **Parameters**:
  - `pk` (path parameter): The unique identifier of the post.
- **Response**: 200 OK
  ```json
  {
    "id": 1,
    "title": "First Post",
    "description": "This is my first post",
    "author": "user1",
    "date": "2023-01-01T12:00:00Z",
    "tags": ["tag1", "tag2"],
    "imageUrl": "https://example.com/image.jpg"
  }
  ```
- **Error Responses**:
  - 404 Not Found: Post with the specified ID does not exist.

##### Update Post
- **URL**: `/api/posts/{pk}/`
- **Method**: PUT
- **Authentication Required**: No
- **Description**: Updates an existing post. The original author of the post is preserved.
- **Parameters**:
  - `pk` (path parameter): The unique identifier of the post.
- **Request Body**:
  ```json
  {
    "title": "Updated Post",
    "description": "This post has been updated",
    "tags": ["tag1", "tag3"],
    "imageUrl": "https://example.com/updated-image.jpg"
  }
  ```
- **Response**: 200 OK
  ```json
  {
    "id": 1,
    "title": "Updated Post",
    "description": "This post has been updated",
    "author": "user1",
    "date": "2023-01-01T12:00:00Z",
    "tags": ["tag1", "tag3"],
    "imageUrl": "https://example.com/updated-image.jpg"
  }
  ```
- **Error Responses**:
  - 400 Bad Request: Invalid data provided.
  - 404 Not Found: Post with the specified ID does not exist.

##### Delete Post
- **URL**: `/api/posts/{pk}/`
- **Method**: DELETE
- **Authentication Required**: No
- **Description**: Deletes an existing post. Any user can delete any post.
- **Parameters**:
  - `pk` (path parameter): The unique identifier of the post.
- **Response**: 204 No Content
- **Error Responses**:
  - 404 Not Found: Post with the specified ID does not exist.

#### Comments

##### List Comments for a Post
- **URL**: `/api/posts/{post_id}/comments/`
- **Method**: GET
- **Authentication Required**: No
- **Description**: Returns a list of all comments for a specific post.
- **Parameters**:
  - `post_id` (path parameter): The unique identifier of the post.
- **Response**: 200 OK
  ```json
  [
    {
      "id": 1,
      "postId": 1,
      "author": "user2",
      "date": "2023-01-01T13:00:00Z",
      "content": "Great post!",
      "likes": 5
    },
    {
      "id": 2,
      "postId": 1,
      "author": "user3",
      "date": "2023-01-01T14:00:00Z",
      "content": "I agree!",
      "likes": 2
    }
  ]
  ```
- **Error Responses**:
  - 404 Not Found: Post with the specified ID does not exist.

##### Create Comment
- **URL**: `/api/posts/{post_id}/comments/`
- **Method**: POST
- **Authentication Required**: No
- **Description**: Creates a new comment for a specific post. The first user in the system will be set as the author.
- **Parameters**:
  - `post_id` (path parameter): The unique identifier of the post.
- **Request Body**:
  ```json
  {
    "content": "This is a new comment",
    "likes": 0
  }
  ```
- **Response**: 201 Created
  ```json
  {
    "id": 3,
    "postId": 1,
    "author": "authenticated_user",
    "date": "2023-01-03T12:00:00Z",
    "content": "This is a new comment",
    "likes": 0
  }
  ```
- **Error Responses**:
  - 400 Bad Request: Invalid data provided.
  - 404 Not Found: Post with the specified ID does not exist.

##### Get Comment Details
- **URL**: `/api/posts/{post_id}/comments/{comment_id}/`
- **Method**: GET
- **Authentication Required**: No
- **Description**: Returns detailed information about a specific comment.
- **Parameters**:
  - `post_id` (path parameter): The unique identifier of the post.
  - `comment_id` (path parameter): The unique identifier of the comment.
- **Response**: 200 OK
  ```json
  {
    "id": 1,
    "postId": 1,
    "author": "user2",
    "date": "2023-01-01T13:00:00Z",
    "content": "Great post!",
    "likes": 5
  }
  ```
- **Error Responses**:
  - 404 Not Found: Post or comment with the specified ID does not exist.

##### Update Comment
- **URL**: `/api/posts/{post_id}/comments/{comment_id}/`
- **Method**: PUT
- **Authentication Required**: No
- **Description**: Updates an existing comment. The original author of the comment is preserved.
- **Parameters**:
  - `post_id` (path parameter): The unique identifier of the post.
  - `comment_id` (path parameter): The unique identifier of the comment.
- **Request Body**:
  ```json
  {
    "content": "Updated comment",
    "likes": 6
  }
  ```
- **Response**: 200 OK
  ```json
  {
    "id": 1,
    "postId": 1,
    "author": "user2",
    "date": "2023-01-01T13:00:00Z",
    "content": "Updated comment",
    "likes": 6
  }
  ```
- **Error Responses**:
  - 400 Bad Request: Invalid data provided.
  - 404 Not Found: Post or comment with the specified ID does not exist.

##### Delete Comment
- **URL**: `/api/posts/{post_id}/comments/{comment_id}/`
- **Method**: DELETE
- **Authentication Required**: No
- **Description**: Deletes an existing comment. Any user can delete any comment.
- **Parameters**:
  - `post_id` (path parameter): The unique identifier of the post.
  - `comment_id` (path parameter): The unique identifier of the comment.
- **Response**: 204 No Content
- **Error Responses**:
  - 404 Not Found: Post or comment with the specified ID does not exist.

### Swagger Documentation

The API also provides Swagger documentation for interactive exploration:

- Swagger UI: `/swagger/`
- ReDoc UI: `/redoc/`
- Swagger JSON: `/swagger.json`
- Swagger YAML: `/swagger.yaml`

## Database Migration: SQLite to PostgreSQL

This project has been updated to use PostgreSQL instead of SQLite. Follow these steps to migrate your data:

### Prerequisites

1. Install PostgreSQL on your system if you haven't already.
2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

### Setting up PostgreSQL

1. Create a new PostgreSQL database:
   ```
   createdb socialnetworkapi
   ```

   Or using psql:
   ```
   psql -U postgres
   CREATE DATABASE socialnetworkapi;
   \q
   ```

2. Configure the database connection in `socialnetworkapi/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'socialnetworkapi',
           'USER': 'postgres',
           'PASSWORD': 'postgres',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

   Adjust the USER, PASSWORD, HOST, and PORT values according to your PostgreSQL setup.

### Migrating Data from SQLite to PostgreSQL

#### Option 1: Using Django's dumpdata/loaddata

1. Dump the data from SQLite:
   ```
   python manage.py dumpdata --exclude auth.permission --exclude contenttypes > data.json
   ```

2. Update the settings.py to use PostgreSQL (as shown above)

3. Run migrations on the PostgreSQL database:
   ```
   python manage.py migrate
   ```

4. Load the data into PostgreSQL:
   ```
   python manage.py loaddata data.json
   ```

#### Option 2: Starting Fresh

If you don't need to migrate existing data:

1. Update the settings.py to use PostgreSQL (as shown above)

2. Run migrations to create the database schema:
   ```
   python manage.py migrate
   ```

3. Create a superuser (if needed):
   ```
   python manage.py createsuperuser
   ```

## Testing the Database Connection

After setting up PostgreSQL and updating the settings, you can test the database connection:

```
python test_db_connection.py
```

If successful, you'll see a message confirming the connection. If not, the script will provide troubleshooting suggestions.

## Running the Application

### Option 1: Running Locally

Start the development server:
```
python manage.py runserver
```

The API will be available at http://127.0.0.1:8000/

### Option 2: Running with Docker

This project is dockerized, allowing you to run it in containers without installing PostgreSQL or Python dependencies directly on your system.

#### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

#### Building and Running

1. Build and start the containers:
   ```
   docker-compose up --build
   ```

   This will build the Django application image and start both the web and database containers. The application will wait for the database to be ready before starting, thanks to the `wait-for-db.sh` script.

2. Run migrations (first time only):
   ```
   docker-compose exec web python manage.py migrate
   ```

3. Create a superuser (optional):
   ```
   docker-compose exec web python manage.py createsuperuser
   ```

The API will be available at http://localhost:8000/

#### Stopping the Containers

To stop the containers:
```
docker-compose down
```

To stop the containers and remove volumes (this will delete the database data):
```
docker-compose down -v
```

#### Environment Variables

The following environment variables can be configured in the `docker-compose.yml` file:

- `DATABASE_HOST`: PostgreSQL host (default: db)
- `DATABASE_NAME`: PostgreSQL database name (default: socialnetworkapi)
- `DATABASE_USER`: PostgreSQL username (default: postgres)
- `DATABASE_PASSWORD`: PostgreSQL password (default: postgres)
- `SECRET_KEY`: Django secret key
- `DEBUG`: Enable/disable debug mode (default: True)
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts (default: localhost,127.0.0.1,0.0.0.0)
