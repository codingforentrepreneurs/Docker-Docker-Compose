
```
docker build -t go-app -f Dockerfile.go-app .
```

```
docker run -p 8084:8000 -e PORT=8000 go-app
```

```
docker run -it --rm go-app /bin/bash
```

```
docker ps
```