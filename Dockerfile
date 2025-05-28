FROM python:3.10-slim

WORKDIR /app

# Install system dependencies for building packages like psutil
RUN apt-get update && apt-get install -y gcc python3-dev && rm -rf /var/lib/apt/lists/*

COPY app/ /app/
COPY app/requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
