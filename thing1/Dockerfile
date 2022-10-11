# syntax=docker/dockerfile:1
FROM python:3.8
COPY . .
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 7776
COPY . /app
CMD ["python3", "-m", "flask", "--app", "thing1.py", "run", "-h", "0.0.0.0", "-p", "7776"]