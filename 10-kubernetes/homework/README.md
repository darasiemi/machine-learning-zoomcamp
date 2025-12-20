Run it to test that it's working locally:

```bash
docker run -it --rm -p 9696:9696 zoomcamp-model:3.13.10-hw10
```

execute the following:
```bash
docker build -f Dockerfile_full -t zoomcamp-model:3.13.10-hw10 .
```

Now let's create a cluster with kind:
```bash
kind create cluster
```

And check with kubectl that it was successfully created:
```bash
kubectl cluster-info
```

To get list of services
```bash
kubectl get services
```
To load image to kind
```bash
kind load docker-image zoomcamp-model:3.13.10-hw10
```
To create resources using the yaml file
```bash
kubectl apply -f deployment.yaml
```
To create service
```bash
kubectl apply -f service.yaml
```
We can test our service locally by forwarding the port 9696 on our computer to the port 80 on the service:
```bash
kubectl port-forward service/subscription 9696:80
```

Use the following command to create the HPA:

```bash
kubectl autoscale deployment subscription --name subscription-hpa --cpu-percent=20 --min=1 --max=3
```
You can check the current status of the new HPA by running:
```bash
kubectl get hpa
```
