FROM python:3.13-slim

COPY main.py .

EXPOSE 80

RUN pip install --no-cache-dir flask requests

ENTRYPOINT ["python", "main.py"]