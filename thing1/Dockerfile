# syntax=docker/dockerfile:1
FROM python:3.10.7
COPY . /thing1
WORKDIR /thing1
RUN pip install --no-cache-dir --compile -r requirements.txt && rm -rf /var/lib/apt/lists/*
EXPOSE 7776
COPY . /app
CMD ["python3", "-m", "flask", "--app", "thing1", "run", "-h", "0.0.0.0", "-p", "7776"]