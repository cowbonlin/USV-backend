# usv-backend
![Python Linter](https://github.com/ARG-NCTU/usv-backend/workflows/Python%20Linter/badge.svg)

The system is under the project Robotx in National Chiao Tung University (Taiwan). Robotx aimed to build an intelligent system for unmanned surface vehicles, and this backend system is responsible for receiving sensor data from vehicles through the MQTT protocol, as well as providing APIs for administrators to access data.

Important parts of the system include a web server with Flask (Python), Database (MySQL), and an MQTT broker.


## Run Services
**Start Services**
```
$ docker-compose up -d
```

**Close Services**
```
$ docker-compose down
```

**Testing**
```
$ docker-compose exec -e FLASK_APP=commands.py web flask test
```

**DB migrations**
```
$ docker-compose exec web flask db migrate -m "message"
$ docker-compose exec web flask db upgrade
```

## Send Files through MQTT
* Event: `image`
* Size Limit: < 268435455 bytes (256 MB)
* File Name Limit: < 256 characters
* File Type: any
* Dest: Files or Images will be storaged in `/images` by default

**Format**
* File Name: File name with right-padding null characters. (256 chars)
* Image Size: Image size with right-padding null characters. (16 chars)
* File Content

**Example**
```
file_name_to_be_sent\0\0\0...\0 (<- total 256 chars)
107\0\0\0...\0 (<- total 16 chars)
\x89\x11\xa4...\x99
```

**Testing**

You can send files to the local mqtt broker with the test client:
```
$ docker-compose exec mqtt-recv python3 mqttrecv/test-sender.py images/test-tosend/example.png
```

## Credits
This system is developed under Dr. Hsueh-Cheng Nick Wang's supervision. If you are intrested in this project, please contact hchengwang@g2.nctu.edu.tw
https://robotx-nctu.github.io/
