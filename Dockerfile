FROM library/python:3.8.6-slim

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

CMD ["python", "/app/aiohttp_prometheus/main.py"]
