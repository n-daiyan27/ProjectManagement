# Django Project

This is a Django project for a collaborative project management tool.

## Setup Instructions

Follow these steps to set up and run the project on your local machine.

### Prerequisites

- Python 3.x
- Django
- Git

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/yourrepository.git
    ```

2. **Navigate to the project directory:**

    ```sh
    cd yourrepository
    ```

3. **Create a virtual environment:**

    ```sh
    python -m venv venv
    ```

4. **Activate the virtual environment:**

    - On Windows:

        ```sh
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```sh
        source venv/bin/activate
        ```

5. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

6. **Run the migrations:**

    ```sh
    python manage.py migrate
    ```

7. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

8. **Start the development server:**

    ```sh
    python manage.py runserver
    ```

## Features

- Project creation and management
- Task addition and updating
- Task assignment to users
- Progress tracking
- User permissions
