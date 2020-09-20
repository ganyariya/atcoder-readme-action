FROM nikolaik/python-nodejs:latest

ADD requirements.txt /requirements.txt
ADD main.py /main.py
ADD getuser.py /getuser.py

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/main.py"]