FROM python:3.11-slim

WORKDIR /app

COPY makePing.py .

RUN pip install requests

CMD ["python", "makePing.py", "10", "http://ping:80/uptime"]
