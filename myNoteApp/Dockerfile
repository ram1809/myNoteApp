# Base image with Python 3.9
FROM python:3.9

# Setting up the working directory
WORKDIR /app

# Copying all files and folders from the host to the Docker file system
COPY . /app

# Installing dependencies
RUN pip install --upgrade pip
RUN pip install --upgrade -r requirements.txt

CMD ["python", "app.py"]
EXPOSE 80

