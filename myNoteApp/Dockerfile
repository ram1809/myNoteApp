#Base image
FROM ubuntu
#setting up work directory
WORKDIR /app
#copy all files and folders from the host to the docker file system
COPY . /app
#installing dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get pip install -r requirements.txt
CMD ["python3", "app.py"]
