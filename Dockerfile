FROM python:3.8-slim

MAINTAINER "nando" <nando@hex7.com>

COPY . .

RUN pip install -r requirements.txt
RUN flask --version

ENV FLASK_APP allgood.py
ENV FLASK_ENV production
ENV FLASK_DEBUG 1

EXPOSE 9999

CMD ["flask", "run", "--host=0.0.0.0", "--port=9999"]
