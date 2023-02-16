FROM python:3.10

ENV PYTHONDONTWRIGHTBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR usr/src/elasticsearch_app

COPY ./req.txt /usr/src/req.txt
RUN pip install -r /usr/src/req.txt

COPY . /usr/src/elasticsearch_app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]