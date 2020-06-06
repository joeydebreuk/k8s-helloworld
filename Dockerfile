FROM python:alpine3.8
COPY server.py /
EXPOSE 7000
CMD ["python", "./server.py"]
