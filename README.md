# Local Community Marketplace API
## Description
This project is an API for a local community marketplace where users can buy, sell, and trade items. The API is built using Django and Django REST Framework, providing user authentication, CRUD operations for listings, search and filter functionality, and a messaging system.

## Project Breakdown
### Day 1: Project Setup
**Project Setup**
- Initialize a Django project and create necessary apps (e.g., profiles, listings, messaging).
- Set up a virtual environment and install dependencies (Django, Django REST Framework).
- Set up version control with Git and push the initial code to GitHub.
- Create a basic README file with project description and setup instructions.

### Installed Apps
INSTALLED_APPS = [
    'profiles',
    'listings',
    'messaging',
    'rest_framework',
    'rest_framework_simplejwt',
    'django_filters'
]

### AUTH_USER_MODEL = 'profiles.Profiles'


### REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
       'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

}

### from datetime import timedelta

### SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=180),  # Access token lifespan
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),    # Refresh token lifespan
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': 'your_secret_key', 
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'TOKEN_TYPE_CLAIM': 'token_type'
}

### User Authentication and Profiles
 User Authentication and Profiles**
- Create Django models for users with profile information (e.g., username, email, bio, profile picture).
- Set up Django API and JWT authentication using libraries like `djangorestframework-simplejwt`.
- Implement API endpoints for user registration, login, logout, and profile management.

### Listings Management
**CRUD Operations for Listings**
- Create Django models for listings (e.g., title, description, price, category, images, user).
- Implement API endpoints for creating, reading, updating, and deleting listings (CRUD).
- Create serializers and views for handling listing data.

### Search and Filter Functionality
** Search and Filter Functionality**
- Implement search functionality to find listings by title, description, and category.
- Add filters for listings based on price range, category, and date of posting.
- Create endpoints for searching and filtering listings.



### Messaging System
**Messaging System**
- Create Django models for messaging (e.g., sender, receiver, listing, content, timestamp).
- Implement API endpoints for sending, reading, and deleting messaging between buyers and sellers.
- Create serializers and views for handling message data.

### Finalizing the Project
**Milestone 6: Finalizing the Project**
- Review and refine code.
- Optimize performance.
- Prepare comprehensive documentation for setup, usage, and API endpoints.
- Test API endpoints using Postman.

## Implementation Details
### Models
1. **User**: Custom user model with profile information (username, email, bio, profile picture).
2. **Listing**: Model to represent marketplace listings (title, description, price, category, images, user).
3. **Message**: Model for messaging between buyers and sellers (sender, receiver, listing, content, timestamp).

### Endpoints
1. **User Authentication and Profiles**: Register, login, logout, manage profiles.
2. **Listings Management**: Create, read, update, delete listings.
3. **Search and Filter**: Search and filter listings based on criteria.
4. **Messaging System**: Send, read, delete messaging.

## Dependencies
 - **Django**: The main framework for web development.
- **Django REST Framework (DRF)**: A powerful and flexible toolkit for building Web APIs.
- **djangorestframework-simplejwt**: For JSON Web Token (JWT) based authentication.
- **Pillow**: For image processing, useful for handling user-uploaded images.
- **django-filter**: For adding filtering capabilities to DRF.
- **django-cors-headers**: To handle Cross-Origin Resource Sharing (CORS) in Django applications.
- **python-decouple**: For managing environment variables.
