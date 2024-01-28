FROM python:3.9

WORKDIR /app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 5000
CMD ["sh", "-c", "cd src && gunicorn -c gunicorn_config.py app:app"]


