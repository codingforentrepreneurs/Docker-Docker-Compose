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



## Pushing to Docker Hub

### 1. Tag images for dockerhub:

Tags must be:
`docker-hub-username`/`reponame`
or
`docker-hub-username`/`reponame:v1`

Such as:

```
docker build -t codingforentrepreneurs/myrepo -f Dockerfile .
```

or 

```
docker build -t codingforentrepreneurs/myrepo:v3 -f Dockerfile .
```

or

```
docker image ls
```
I have an image with the id of `f52105e1ba2b` that I am going to tag to `codingforentrepreneurs/docker-dc-goapp`

```
docker tag f52105e1ba2b codingforentrepreneurs/docker-dc-goapp
```

The format is 
```
docker tag <built-image-id> <new-tag>
```

### 2. Push with new tag:

```
docker push <new-tag>
```
like
```
docker push codingforentrepreneurs/docker-dc-goapp
```
