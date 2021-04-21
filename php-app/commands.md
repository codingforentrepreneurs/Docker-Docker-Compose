
```
docker build -t php-app -f Dockerfile.php-app .
```

```
docker run -p 8083:8001 -e PORT=8001 php-app
```

```
docker run -it --rm php-app /bin/bash
```

```
docker ps
```