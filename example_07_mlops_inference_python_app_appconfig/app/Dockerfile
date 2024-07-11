FROM python:3.8

RUN pip install pandas
RUN pip install numpy
RUN pip install requests

RUN  mkdir /APP
COPY app.py .

CMD ["python3","-u","app.py"]

