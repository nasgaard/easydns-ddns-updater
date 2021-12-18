FROM python:2

WORKDIR /usr/src/app

RUN pip install requests

COPY ddns.py /

CMD ["python", "-u", "/ddns.py"]
