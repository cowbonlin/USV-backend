FROM python:3.7.7
ENV TZ=Asia/Taipei

WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--worker-class", "eventlet", "--workers", "1", "app:app"]
