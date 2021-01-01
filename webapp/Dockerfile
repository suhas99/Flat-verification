# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image

FROM python:3.8.1

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /djangocode

# Set the working directory to /djangocode
WORKDIR /djangocode

# Copy the current directory contents into the container at /djangocode
ADD . /djangocode/

# RUN python -m venv env

CMD ["source env/bin/activate"]

# RUN pip install -r requirements.txt