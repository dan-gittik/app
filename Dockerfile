FROM python:latest
MAINTAINER Dan Gittik <dan.gittik@gmail.com>

COPY app/ /app/
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

EXPOSE 8000

CMD ['python', '-m', 'app', 'run']
