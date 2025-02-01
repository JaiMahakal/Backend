# Backend
# Django FAQ API

## Installation
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver`

## API Usage
- **GET** /api/faqs/?lang=hi

## Contribution Guidelines
1. Fork the repository.
2. Create a new branch.
3. Commit changes with conventional messages.
4. Open a pull request.

## Testing
Run tests using:
```bash
pytest
flake8
### 9. Git & Version Control
- Use clear and conventional commit messages:
  - `feat: Add multilingual FAQ model`
  - `fix: Improve translation caching`
  - `docs: Update README with API examples`

**Branching Strategy:**
- Use feature branches for development.

### 10. Deployment & Docker Support (Bonus)
**Docker Configuration:**
- Provide `Dockerfile` and `docker-compose.yml`.

#### Example Dockerfile
```Dockerfile
FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
