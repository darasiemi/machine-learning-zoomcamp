To run docker image
```bash
docker build -t hair-lambda .
docker run -it --rm -p 8080:8080 hair-lambda
```

To create ecr repository
```bash
aws ecr create-repository \
  --repository-name "hair-prediction-lambda" \
  --region "eu-north-1"
```
