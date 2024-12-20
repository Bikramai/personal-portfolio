
# Bikram's Site


## Prerequisites

Make sure the following are installed on your machine:
- **Python 3.11+**
- **pip** (Python package manager)
- **virtualenv** (for creating an isolated Python environment)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/yourprojectname.git
cd yourprojectname
```

### 2. Set Up a Virtual Environment

Create a virtual environment to isolate dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

Use `pip` to install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

To set up the database, run the following commands:

```bash
python manage.py makemigrations website core
python manage.py migrate
```

### 5. Create a Superuser (Optional)

If you need admin access, create a superuser with:

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The project should now be accessible at `http://127.0.0.1:8000/`.

---

## Additional Commands

### Running Tests

Run tests (if available) with:

```bash
python manage.py test
```

### Linting and Code Quality

(Optional) Use tools like `flake8` or `black` to maintain code quality:

```bash
flake8 .
black .
```

---

## Deployment

For production, set up configurations for `ALLOWED_HOSTS`, database settings, and static files. Refer to the Django documentation for further deployment instructions.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Happy Coding !hshm*