# syntax=docker/dockerfile:1
FROM python:3.10.7
COPY . .
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir --compile -r requirements.txt && rm -rf /var/lib/apt/lists/*
EXPOSE 7777
COPY . /app
CMD ["python3", "-m", "flask", "--app", "thing2.py", "run", "-h", "0.0.0.0", "-p", "7777"]