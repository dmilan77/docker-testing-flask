```
docker build -t dmilan/docker-sample-restapp-flask .
docker run -it -p 8080:8080 dmilan/docker-sample-restapp-flask
kubectl exec -it $(kubectl get pod -l app=sample-restapp -o jsonpath='{.items[0].metadata.name}') -c sample-restapp -- curl sample-restapp-service-clusterip/ping
curl localhost:8080/ping
```
