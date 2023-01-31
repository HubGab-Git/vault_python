FROM python:3.9.16-alpine

COPY app.py app.py

RUN pip install hvac

CMD ["python", "app.py"]