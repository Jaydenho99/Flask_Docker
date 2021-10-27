FROM python:3.8
WORKDIR /trial
ADD . /Flask_Docker
RUN pip install -r requirements.txt
CMD["python","app.py"]