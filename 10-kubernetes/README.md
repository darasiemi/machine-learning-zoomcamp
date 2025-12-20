To install kind
```bash
brew install kind
```
To initialize uv
```bash
uv init
```
To install libraries
```bash
uv add fastapi uvicorn onnxruntime keras-image-helper numpy
```
To run the service
```bash
uv run uvicorn app:app --host 0.0.0.0 --port 8080 --reload
```
To check the health of the application
```bash
curl localhost:8080/health
```

### Docker
```bash
docker build -t clothing-classifier:v1 .
```

```bash
docker run -it --rm -p 8080:8080 clothing-classifier:v1
```

### Create a Kind cluster
```bash
kind create cluster --name mlzoomcamp
```
Verify the cluster is running
```bash
kubectl cluster-info
kubectl get nodes
```
### Loading image into kind
Kind clusters run in Docker, so they can't access images from your local Docker daemon by default. We need to load the image into Kind.


```bash
kind load docker-image clothing-classifier:v1 --name mlzoomcamp
```
To create resources using the yaml file
```bash
kubectl apply -f deployment.yaml
```

To get pods
```bash
kubectl get pods
```

To see what is happening in the pod
```bash
kubectl describe pod <pod>
```

To create service
```bash
kubectl apply -f service.yaml
```

To get services
```bash
kubectl get services
```
Our kind cluster is not configured for NodePort, so it won't work. We don't really need this for testing things locally, so let's just use a quick fix: Use kubectl port-forward.
```bash
kubectl port-forward service/clothing-classifier 30080:8080
```

Check the health endpoint
```bash
curl http://localhost:30080/health
```

To create horizontal pod autoscaler
```bash
kubectl apply -f hpa.yaml
```

To check how many deployments you have
```bash
kubectl get deployments
```

### HPA
To check hpa
```bash
kubectl get hpa
```
First, we need metrics-server for HPA to work. Install it in kubectl:
```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```
For Kind, we need to patch metrics-server to work without TLS:
```bash
kubectl patch -n kube-system deployment metrics-server --type=json -p '[{"op":"add","path":"/spec/template/spec/containers/0/args/-","value":"--kubelet-insecure-tls"}]'
```

To run stress test
```bash
uv run python load_test.py
```