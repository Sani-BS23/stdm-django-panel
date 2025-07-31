# Todo Project

A Django REST API for managing student todos with PostgreSQL database support.

## Features

- Student management with dynamic todo tracking
- Todo creation, updating, and deletion via RESTful API
- Automatic tracking of completed todos per student
- PostgreSQL database integration

## Prerequisites

- Python 3.10+
- PostgreSQL 12+
- pip (Python package manager)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/todo_project.git
cd todo_project
```

### 2. Create Virtual Environment

```bash
python -m venv env
```

Activate the virtual environment:

- On Windows:
  ```bash
  env\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source env/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

- Install PostgreSQL if you haven't already
- Create a database for the project:

```bash
createdb todo_db
```

### 5. Configure Environment Variables

Create a `.env` file in the project root with the following variables:

```
DEBUG=True
SECRET_KEY=your_secret_key_here
DB_NAME=todo_db
DB_USER=your_db_username
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

### 6. Run Migrations

```bash
cd todo_project
python manage.py migrate
```

### 7. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

The API will be available at http://127.0.0.1:8000/

## API Endpoints

- GET/POST `/todo/` - List all todos or create a new todo
- GET/PUT/DELETE `/todo/<id>/` - Get, update or delete a specific todo
- GET `/student/` - List all students with their completed todo count

## Project Structure

```
todo_project/
├── manage.py          # Django management script
├── todo_project/      # Project settings
├── student/           # Student app
└── todos/             # Todos app
```

## Database Schema

- **Student**: Stores student information
    - name
    - email
    - (virtual) done_count

- **Todo**: Stores todo items
    - title
    - slug
    - content
    - completed
    - created_at
    - updated_at
    - student (ForeignKey to Student)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
