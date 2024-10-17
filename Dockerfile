# start from python base image
FROM python:3.12.3

# change working directory
WORKDIR /code

# add requirements file to image
COPY ./requirements.txt /code/requirements.txt

# install python libraries
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# add python code
COPY ./app/ /code/app/

EXPOSE 80

# specify default commands
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]