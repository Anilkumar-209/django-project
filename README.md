# Project Setup Instructions

## Prerequisites
- Docker & Docker Compose
- Python 3.9+
- MySQL 8+
- Redis 7+

## Local Development

1. **Clone the repository**
2. **Create and activate a virtual environment:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```
4. **Configure environment variables** (optional, see `docker-compose.yml` for defaults)
5. **Run migrations:**
   ```powershell
   python manage.py migrate
   ```
6. **Run the development server:**
   ```powershell
   python manage.py runserver
   ```
7. **Start Celery worker (in a new terminal):**
   ```powershell
   celery -A backend worker -l info
   ```
8. **Start Celery beat (in a new terminal):**
   ```powershell
   celery -A backend beat -l info
   ```

## Dockerized Development

1. **Build and start all services:**
   ```powershell
   docker-compose up --build
   ```

## API Documentation
- Swagger UI: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
- OpenAPI schema: [http://localhost:8000/api/schema/](http://localhost:8000/api/schema/)

## User APIs
- `POST /api/users/register/` — Register a new user
- `POST /api/users/login/` — Obtain JWT token

## Paragraph APIs
- `POST /api/paragraphs/input/` — Input multiple paragraphs (separated by two newlines)
- `GET /api/paragraphs/search/?word=example` — Get top 10 paragraphs with max occurrences of a word

## Code Documentation
- All modules and classes are documented inline.

---

For any issues, please refer to the code comments and API docs.
