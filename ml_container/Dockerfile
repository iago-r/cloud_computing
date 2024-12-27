FROM python:3.9-slim-bullseye

WORKDIR /app
RUN mkdir -p /models

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY playlist_recommender.py .

CMD ["python", "playlist_recommender.py"]