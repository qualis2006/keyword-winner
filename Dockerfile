FROM python:3

COPY . /app

RUN pip3 install flask requests bs4 lxml 

WORKDIR /app

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]