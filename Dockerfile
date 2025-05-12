FROM python:3.10-slim

#PYTHONDONTWRITEBYTECODE 1: Prevents Python from generating .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

#PYTHONUNBUFFERED 1: Ensures Python output is sent straight to terminal
ENV PYTHONUNBUFFERED 1

WORKDIR /app


#Installs system-level packages needed for Python dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    gcc \
    && rm -rf /var/lib/apt/lists/*



COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
#--no-cache-dir: Reduces image size by not storing pip cache


COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn","--bind","0.0.0.0:8000","webchat.wsgi:application"]

