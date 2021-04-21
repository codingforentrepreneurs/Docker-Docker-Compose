
```
docker build -t php-app -f Dockerfile.php-app .
```

```
docker run -p 8083:8000 -e PORT=8000 php-app
```

```
docker run -it --rm php-app /bin/bash
```

```
docker ps
```