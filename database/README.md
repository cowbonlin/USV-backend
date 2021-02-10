# Create a new MySQL Database with docker-compose

1. Go to `/usv-backend/`
2. Create a new `docker-compose.override.yml` file in `/usv-backend/` with the following content:
```
version: '3'
services:
    db:
        ports:
            - 3306:3306
```

The above setting will create db on port 3306, which is the default mysql port. If you want to create db on the other port(e.g. 3308), type the following content into `docker-compose.override.yml`:

```
version: '3'
services:
    db:
        ports:
            - 3308:3306
```

3. Copy the file from [Google Drive](https://drive.google.com/file/d/1SMgltOM-3jmbUXtuOXaSXscRyFnI8o7E/view?usp=sharing), and move it into `/usv-backend/db/`. 
The file stores username and password of mysql users, so keep it in a safe place.

4. In /usv-backend, run `docker-compose up -d db`
The command will build a mysql container in daemon. To see the logs of the container, run `docker-compose logs -f db`.

5. Login to the mysql shell. run `docker-compose exec db mysql -urobotxuser -p`, and type the password stored in `/user-backend/db/secret.env`

6. To close the mysql server, run `docker-compose down db`. Data stored in db won't be deleted and it can be accessed again after db container is opened again.
If you want to delete the data as well, run `docker-compose down db -v`.

---
To wrap up, Two files (`docker-compose.override.yml` and `secret.yml`) needed to be created by yourself if you want to start the mysql service in the first place.
A simple folder structure is presented below:
```
usv-backend/
├── db/
│   ├── screte.env
│   └── ...
├── docker-compose.override.yml
└── ...
```

Besides, every `docker-compose` commands must be executed inside /usv-backend/ folder which contains `docker-compose.yml` file. Errors will show if you execute `docker-compose` commands in the other folder.
