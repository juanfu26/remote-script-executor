FROM python:3.10-slim

RUN pip install paramiko

RUN mkdir /app
COPY scripts /app/scripts

WORKDIR /app/scripts

CMD ["python", "executor.py"]