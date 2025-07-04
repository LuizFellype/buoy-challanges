# Django Tech Challenge - Accommodation Booking API

Welcome to the Django implementation of Buoy's accommodation booking tech challenge!

This repository contains a **partially implemented accommodations booking REST API**, designed as a work-in-progress prototype for a real-world application.

You must use the provided code sample and its dependencies to solve the problems explained below.

The solution must be a cloud git repository, hosted on any cloud git tool of your choice.

- Its first commit must:
  - Have the message "First commit"
  - Have the exact code sample as it was provided, no changes whatsoever
- From this point on, work on the problems exposed below as you like

NOTE: In case you want to create a private git repository, please grant the user matthew@buoydevelopment.com full access to the repo. If you do so, please make it clear once you reply with your answer.

---

# Problem #1

### Issue to solve

There's an Accommodations entity already in place, however the business model only includes Hotels and Apartments.

### Expected behaviour

- Add these 2 new entities to the project.
- Provide endpoints for their management.

# Problem #2

### Issue to solve

Currently, every Accommodation can contain several overlapping Bookings with the same `start_date` and `end_date`. This makes sense for Hotels, which can have different Rooms booked simultaneously, but it wouldn't work for Apartments.

### Expected behaviour

- Apartments should not allow overlapping bookings during the same period (`start_date` and `end_date`).
- Hotels should allow overlapping bookings during the same period, as these would correspond to bookings for different rooms within the hotel.

# Problem #3

### Issue to solve

If frontend needs to, given an accommodation's `id` and a `date`, retrieve the next available date for that accommodation.

### Question

- How would you solve this problem?
- What data or API would you provide to the frontend?

## TECH CONTEXT
### Stack

The main libraries are:
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django ORM](https://docs.djangoproject.com/en/5.0/topics/db/)

### Docker Setup
To set up the project using Docker Compose, follow these steps:

1. Ensure you have Docker and Docker Compose installed on your machine.
2. Build and start the Docker containers:

  ```bash
  docker compose up --build
  ```

3. The application should now be running and accessible at `http://localhost:8006`.

### Swagger Documentation

The interactive API documentation is available at:
```
http://localhost:8006/documentation/
```

### Migrations

Migrations are automatically applied when the Docker containers start via the `entrypoint.sh` script.

For manual migration management during development:

#### Migration creation
1. Stop the web container: `docker compose stop web`
2. Run the migration creation command: 
   ```bash
   docker compose run --rm web python manage.py makemigrations
   ```
3. Restart containers: `docker compose up`

#### Manual Migration Up
```bash
docker compose run --rm web python manage.py migrate
```

#### Manual Migration Down
```bash
docker compose run --rm web python manage.py migrate <app_name> <migration_number>
```

## 🚀 Current Implementation

### Available Endpoints
#### Accommodations
- `GET /accommodations/` - List all accommodations
- `POST /accommodations/` - Create accommodation
- `GET /accommodations/{id}/` - Get accommodation by ID
- `PUT /accommodations/{id}/` - Update accommodation
- `DELETE /accommodations/{id}/` - Delete accommodation

#### Hotels
- `GET /accommodations/hotels/` - List all hotels
- `POST /accommodations/hotels/` - Create hotel
- `GET /accommodations/hotels/{id}/` - Get hotel by ID
- `PUT /accommodations/hotels/{id}/` - Update hotel
- `DELETE /accommodations/hotels/{id}/` - Delete hotel

#### Apartments
- `GET /accommodations/apartments/` - List all apartments
- `POST /accommodations/apartments/` - Create apartment
- `GET /accommodations/apartments/{id}/` - Get apartment by ID
- `PUT /accommodations/apartments/{id}/` - Update apartment
- `DELETE /accommodations/apartments/{id}/` - Delete apartment

#### Bookings
- `GET /bookings/` - List all bookings
- `POST /bookings/` - Create booking
- `GET /bookings/{id}/` - Get booking by ID
- `PUT /bookings/{id}/` - Update booking
- `DELETE /bookings/{id}/` - Delete booking
- `GET /bookings/availability/?accommodation_id={id}&date={date}` - Get next available date for an accommodation (date format: YYYY-MM-DD)

### Key Features & Business Logic

- **Accommodation Types**: The API supports three types: Accommodation (base), Hotel, and Apartment. Hotels and Apartments inherit from Accommodation.
- **Overlapping Bookings**: 
  - **Apartments**: Do **not** allow overlapping bookings for the same period.
  - **Hotels**: Allow overlapping bookings (multiple rooms can be booked for the same dates).
- **Next Available Date**: 
  - Endpoint `/bookings/{accommodation_id}/next-available-date/{date}/` returns the next available date for a given accommodation after a specified date.
  - Returns `{"next_available_date": "YYYY-MM-DD"}`.

### Data Models

#### Accommodation (Base Model)
```json
{
    "id": 1,
    "name": "Luxury Hotel Downtown",
    "description": "A beautiful hotel in the city center",
    "price": "150.00",
    "location": "Downtown"
}
```

#### Hotel
```json
{
    "id": 2,
    "name": "Grand Hotel",
    "description": "A grand hotel",
    "price": "200.00",
    "location": "Uptown",
    "number_of_rooms": 100
}
```

#### Apartment
```json
{
    "id": 3,
    "name": "City Apartment",
    "description": "A cozy apartment",
    "price": "120.00",
    "location": "Midtown",
    "floor_number": 5
}
```

#### Booking
```json
{
    "id": 1,
    "accommodation": 1,
    "start_date": "2024-02-01",
    "end_date": "2024-02-05",
    "guest_name": "John Doe"
}
```

## 🔧 Development Setup

### Docker Development (Recommended)

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd tech-challenge-python
   ```

2. **Start with Docker Compose**:
   ```bash
   docker compose up --build
   ```

3. **Access the application**:
   - API: `http://localhost:8006`
   - Documentation: `http://localhost:8006/documentation/`
   - Admin: `http://localhost:8006/admin/`

### Local Development (without Docker)

1. **Prerequisites**:
   - Python 3.11+
   - PostgreSQL 15+

2. **Install PostgreSQL** (if not already installed):
   ```bash
   # macOS with Homebrew
   brew install postgresql
   brew services start postgresql
   
   # Ubuntu/Debian
   sudo apt-get update
   sudo apt-get install postgresql postgresql-contrib
   sudo systemctl start postgresql
   
   # Windows - Download from https://www.postgresql.org/download/windows/
   ```

3. **Create database**:
   ```bash
   # Connect to PostgreSQL as superuser
   sudo -u postgres psql
   
   # Or on macOS/Windows where postgres user might be your username:
   psql postgres
   
   # Create database and user
   CREATE DATABASE accommodation_booking;
   CREATE USER postgres WITH ENCRYPTED PASSWORD 'postgres';
   GRANT ALL PRIVILEGES ON DATABASE accommodation_booking TO postgres;
   \q
   ```

4. **Setup Python environment**:
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

5. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

6. **Configure environment**:
   ```bash
   cp env.example .env
   # Edit .env file with your database settings if different from defaults
   ```

7. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

8. **Create superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

9. **Start development server**:
   ```bash
   python manage.py runserver 8006
   ```

10. **Access the application**:
    - API: `http://localhost:8006`
    - Documentation: `http://localhost:8006/documentation/`
    - Admin: `http://localhost:8006/admin/` (if superuser created)

## 📁 Project Structure

```
tech-challenge-python/
├── accommodation_booking/     # Django project settings
│   ├── __init__.py
│   ├── settings.py           # Configuration with PostgreSQL
│   ├── urls.py              # Main URL routing
│   ├── wsgi.py              # WSGI application
│   └── asgi.py              # ASGI application
├── accommodations/           # Accommodations app
│   ├── migrations/          # Database migrations
│   ├── models/          # Database migrations
│   │   ├── __init__.py
│   │   ├── accomodation.py
│   │   ├── hotel.py
│   │   ├── apartment.py
│   ├── models.py            # exporting all models
│   ├── serializers.py       # DRF serializers with validation
│   ├── views.py            # export all views
│   │   ├── __init__.py
│   │   ├── accomodation.py
│   │   ├── hotel.py
│   │   ├── apartment.py
│   ├── urls.py             # URL routing
│   ├── admin.py            # Admin configuration
│   └── apps.py             # App configuration
├── bookings/                # Bookings app
│   ├── migrations/          # Database migrations
│   ├── models.py           # Booking model
│   ├── serializers.py      # Booking serializers
│   ├── views.py           # Booking CRUD operations
│   ├── urls.py            # URL routing
│   ├── admin.py           # Admin configuration
│   └── apps.py            # App configuration
├── requirements.txt        # Python dependencies
├── docker compose.yml     # Docker services configuration
├── Dockerfile            # Docker image definition
├── entrypoint.sh         # Docker entrypoint script
├── env.example          # Environment variables template
├── manage.py           # Django management commands
└── README.md          # This documentation
```

## 🌐 Environment Variables

Create a `.env` file based on `env.example`:

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `DEBUG` | Enable debug mode | `True` | No |
| `SECRET_KEY` | Django secret key | `django-insecure-your-secret-key-here` | Yes (change in production) |
| `DB_HOST` | Database host | `localhost` | No |
| `DB_PORT` | Database port | `5432` | No |
| `DB_NAME` | Database name | `accommodation_booking` | No |
| `DB_USER` | Database user | `postgres` | No |
| `DB_PASSWORD` | Database password | `postgres` | No |

## 🧪 Testing the API

You can test the API using the interactive documentation at `http://localhost:8006/documentation/` or use curl:

```bash
# List accommodations
curl http://localhost:8006/accommodations/

# Create an accommodation
curl -X POST http://localhost:8006/accommodations/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Hotel",
    "description": "A test hotel",
    "price": "100.00",
    "location": "Test City"
  }'

# List bookings
curl http://localhost:8006/bookings/

# Create a booking (replace {accommodation_id} with actual ID)
curl -X POST http://localhost:8006/bookings/ \
  -H "Content-Type: application/json" \
  -d '{
    "accommodation": 1,
    "start_date": "2024-03-01",
    "end_date": "2024-03-05",
    "guest_name": "John Doe"
  }'
```

## 🚨 Current Dependencies

The project uses the following key dependencies (see `requirements.txt` for versions):

- `Django==5.0.0` - Web framework
- `djangorestframework==3.14.0` - REST API framework
- `psycopg2-binary==2.9.9` - PostgreSQL adapter
- `drf-spectacular==0.27.0` - API documentation
- `django-cors-headers==4.3.1` - CORS handling
- `python-dotenv==1.0.0` - Environment variable management 