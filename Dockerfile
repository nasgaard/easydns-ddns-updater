FROM python:3.10-slim-buster

WORKDIR /usr/src/app

RUN pip install requests

COPY ddns.py /

CMD ["python", "-u", "/ddns.py"]
