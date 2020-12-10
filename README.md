# usv-backend

## Start Services 
### Dev
```
$ docker-compose up -d
```
### Prod
```
$ docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```
## Close Services
```
$ docker-compose down
```

## Testing
```
$ docker exec -it -e FLASK_APP=commands.py usv-backend_web_1 flask test
```

## DB migrations
```
$ docker exec -it usv-backend_web_1 flask db migrate -m "migration information"
$ docker exec -it usv-backend_web_1 flask db upgrade
```
