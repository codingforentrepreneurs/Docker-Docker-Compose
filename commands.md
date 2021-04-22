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