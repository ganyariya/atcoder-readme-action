FROM nikolaik/python-nodejs:latest

ADD requirement.txt /requirement.txt
ADD main.py /main.py

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/main.py"]