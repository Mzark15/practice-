FROM python:3.8-slim-buster

WORKDIR /flask-docker
RUN python3 -m pip install --upgrade pip 
COPY requirments.txt requirments.txt
# -r ----> read from the requirments file
RUN pip3 install -r requirments.txt
#first (.) for entire local machine files and second(.) for files in container(./flask-docker)
COPY . .

#final command for run the flask application
CMD ["python3","-m","flask","run","--host=0.0.0.0"]
