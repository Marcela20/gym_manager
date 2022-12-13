FROM ubuntu:latest

ARG USER_ID
ARG GROUP_ID 

RUN apt-get -y update
RUN apt-get install -y sqlite3 python3 python3-pip python3.10-venv
ENV PYTHONUNBUFFERED=1
RUN addgroup --gid $GROUP_ID user
RUN adduser -disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user
# ENV DockerHOME=/home/mchrusto/gym_backend/
# ENV PATH="/home/mchrusto/.local/bin:/usr/local/bin/python3:/usr/bin/python3:${PATH}"

# RUN mkdir -p $DockerHOME 

# WORKDIR $DockerHOME

USER user
# RUN chown -R 1001:1001 $DockerHOME

# RUN export PATH=$PATH:/home/mchrusto/.local/bin
# ADD . .   
# USER root
# RUN chown -R 1001:1001 $DockerHOME
# RUN chown -R 1001:1001 $DockerHOME/db.sqlite3
# RUN chmod 777 $DockerHOME
# RUN chmod 777 $DockerHOME/db.sqlite3  
USER root
ADD . .
RUN pip install -r requirements.txt
USER user


EXPOSE 8000
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
