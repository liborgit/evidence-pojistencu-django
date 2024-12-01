# Insured People Management - Django

This project is a full-stack web application designed for managing insured people using the Django framework. It allows users to easily and efficiently add, edit, search, and view information about insured individuals.

## Features
- Add a new insured person
- Display a list of all insured people
- Search for an insured person by first name and last name
- Edit and update information about insured people

## Technology Stack
The project is built using the following technologies:
- **Django** (Python web framework)
- **SQL** (Database)
- **HTML**, **CSS**, **JavaScript**

## Deployment
The project is deployed online and can be accessed at: [https://liboroliva.pythonanywhere.com/](https://liboroliva.pythonanywhere.com/)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/liborgit/insured-people-management.git
   ```

2. Navigate to the project directory:
    ```bash
    cd insured-people-management/src
    ```

3. Install the dependencies from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file and add the following environment variables:
    ```makefile
    DJANGO_SECRET_KEY=...
    DJANGO_DEBUG=False
    DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost,...
    ```

5. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```
    
