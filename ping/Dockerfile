FROM python:3.13-slim

COPY app.py .

RUN pip install --no-cache-dir flask psycopg2-binary

EXPOSE 5000

CMD ["python", "app.py"]
