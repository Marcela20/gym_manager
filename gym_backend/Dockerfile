FROM  python:3.8

ENV PYTHONUNBUFFERED=1

ENV DockerHOME=/home/backend/gym_backend/

RUN mkdir -p $DockerHOME  
WORKDIR $DockerHOME

RUN pip install --upgrade pip 

COPY  . . 
RUN chown -R root:root .

RUN pip install -r requirements.txt


EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
# FROM python:3.10-alpine
# ENV PYTHONUNBUFFERED 1
# RUN apk update \
#     && apk add postgresql-dev gcc python3-dev musl-dev
# RUN pip install --upgrade pip pipenv
# WORKDIR /gym_backend
# COPY ./Pipfile* ./
# RUN pipenv sync
# COPY . .
# COPY ./entrypoint.sh /entrypoint.sh
# RUN chmod o+x /entrypoint.sh
# ENTRYPOINT ["sh", "-c", "/entrypoint.sh"]