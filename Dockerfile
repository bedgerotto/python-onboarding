# set base image (host OS)
FROM python:3.9
# set the working directory in the container
WORKDIR /code

# command to run on container start
CMD [ "bash" ]
