FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
 
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt --no-cache-dir

RUN apk --purge del .build-deps 