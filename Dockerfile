FROM python:3.7.3
EXPOSE $APP_PORT

COPY . /srv/tornado/schedule-DB
WORKDIR /srv/tornado/schedule-DB
RUN pip install -r requirements.txt

ENV PYTHONPATH=src
ENTRYPOINT ["python", "app/main.py"]