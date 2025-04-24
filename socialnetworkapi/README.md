# Social Network API

This is a Django-based REST API for a social network application.

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
