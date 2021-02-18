FROM python:3.7.7
ENV TZ=Asia/Taipei

ARG REQ_TXT
WORKDIR /src
COPY ${REQ_TXT:-requirements.txt} .
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000