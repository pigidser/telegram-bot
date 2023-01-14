FROM python:3.8

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip && pip install pip install psycopg2-binary==2.9.3 && pip install -r requirements.txt

WORKDIR /app

EXPOSE 8000

COPY wsgi.py wsgi.py
COPY app.py app.py

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app"]