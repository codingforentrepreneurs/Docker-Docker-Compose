```
docker compose build --no-cache
```


```
docker compose up --build
```

```
docker compose down
```



Delete all containers
```
docker rm -vf $(docker ps -a -q)
```

Delete all images
```
docker rmi -f $(docker images -a -q)
```
Found [here](https://stackoverflow.com/a/44785784)





Automated Volume Creation
```
docker run -v myvol:/where/to/mount container-image
```
> `docker run --name ironman-1 -v ironmanvol:/app/data3 py-app-1`
```
docker volume ls 
```

Manual Volume Creation
```
docker run -v /abs/path/to/local/data/:/where/to/mount/ py-app-1
```
> `docker run --name ironman -v /Users/cfe/Dev/docker-dc/data/:/app/data  py-app-1`



### Databases

```
docker pull postgres
```


```
docker run -p 6543:5432 -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mytestpw  postgres
```

```
docker run -it --rm postgres /bin/bash
# psql -U myuser
```