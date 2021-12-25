FROM python:ddns

COPY ddns.py /

CMD ["python", "-u", "/ddns.py"]
