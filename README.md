# Blog Backend API

This is the backend API for the Blog application, built using **Django** and **Python**. It serves as the backend for a blog platform, providing endpoints for managing posts, users, and likes.

## Features

- User authentication and management
- CRUD operations for posts
- Like and view tracking for posts
- Post publishing and editing functionality
- Secure API with JWT token-based authentication

## Technologies Used

- **Django**: A Python-based web framework for building the backend.
- **Django Rest Framework**: A powerful toolkit for building Web APIs in Django.
- **PostgreSQL**: Database used for storing data.
- **JWT (JSON Web Tokens)**: Used for secure user authentication.
- **Django-Allauth**: For handling user authentication and registration.
- **Docker**: Used for containerization of the application.

## Installation

### Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.x
- pip (Python package installer)
- PostgreSQL (or any database configured for the project)

### Steps

1. **Clone the repository**:

    ```bash
    git clone https://github.com/assimad8/blog-backend.git
    cd blog-backend
    ```

2. **Create a virtual environment**:

    ```bash
    python3 -m venv venv
    ```

3. **Activate the virtual environment**:

    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Set up the database**:

    Make sure your Postgr
