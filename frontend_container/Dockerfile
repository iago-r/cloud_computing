FROM python:3.9-slim-bullseye

RUN mkdir -p /models
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 52030
CMD ["flask", "run", "--host=0.0.0.0"]