```
docker build -t dmilan/docker-sample-restapp-flask .
docker run -it -p 8080:8080 dmilan/docker-sample-restapp-flask
curl localhost:8080/ping
```
