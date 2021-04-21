
```
docker build -t express-app -f Dockerfile.express-app .
```

```
docker run -p 8082:8000 -e PORT=8000 express-app
```

```
docker run -it --rm express-app /bin/bash
```

```
docker ps
```