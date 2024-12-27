FROM python:3.9-slim-bullseye

WORKDIR /app
RUN mkdir -p /app/models

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN mkdir -p /app/assets

EXPOSE 52030

CMD ["flask", "run", "--host=0.0.0.0"]