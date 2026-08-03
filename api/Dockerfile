FROM python:3.12-slim

workdir /app

copy requirements.txt .

run pip install --no-cache-dir -r requirements.txt

copy . .

expose 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]