FROM nikolaik/python-nodejs:latest

ADD requirements.txt /requirements.txt
ADD main.py /main.py
ADD insert_text.py /insert_text.py

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/main.py"]