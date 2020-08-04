# Dockerfile
FROM python:3.8-slim-buster

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

RUN useradd --create-home appuser && mkdir -p /home/logs && chown -R appuser /home/logs

WORKDIR /home/appuser

USER appuser

COPY ./app /home/appuser

#CMD [ "flask", "run", "--host=0.0.0.0" ]