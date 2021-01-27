# usv-backend
![Python Linter](https://github.com/ARG-NCTU/usv-backend/workflows/Python%20Linter/badge.svg)

## Start Services 
### Dev and Prod
```
$ docker-compose up -d
```

## Close Services
```
$ docker-compose down
```

## Testing
```
$ docker-compose exec -e FLASK_APP=commands.py web flask test
```

## DB migrations
```
$ docker-compose exec web flask db migrate -m "message"
$ docker-compose exec web flask db upgrade
```
