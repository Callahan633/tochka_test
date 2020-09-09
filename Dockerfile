# pull official base image
FROM python:3.8.3-alpine
# set work directory
WORKDIR /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev busybox-initscripts
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# copy init_db.sh
COPY ./init_db.sh .
# copy project
COPY . .
RUN ["chmod", "+x", "/usr/src/app/init_db.sh"]
# run init_db.sh
ENTRYPOINT ["/usr/src/app/init_db.sh"]
