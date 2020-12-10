FROM python:3.7.7
ENV TZ=Asia/Taipei

WORKDIR /src
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 8000
