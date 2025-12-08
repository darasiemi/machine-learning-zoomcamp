To initialize uv
```bash
uv init
```

To install libraries
```bash
uv add scikit-learn pandas
```

To run train.py
```bash
uv run python train.py
```

To run invoke.py, first install boto3
```bash
pip install boto3
```

Then run invoke.py
```bash
python invoke.py
```
### AWS Lambda with Docker: Running Locally
To build Docker image
```bash
docker build -t churn-prediction-lambda .
```

To run Docker container
```bash
docker run -it --rm -p 8080:8080  churn-prediction-lambda
```

### AWS Lambda: Deployment
It's time to deploy our Lambda to AWS.

Since we use Docker, we'll need to create a registry

You can do it through the web interface, but we'll save time and do it with AWS CLI:
```bash
aws ecr create-repository \
  --repository-name "churn-prediction-lambda" \
  --region "eu-north-1"
```
Let's put the ECR URL into a variable:
```bash
ECR_URL="511900348839.dkr.ecr.eu-north-1.amazonaws.com"
```
Now login to that repo with Docker:
```bash
aws ecr get-login-password \
  --region "eu-north-1" \
| docker login \
  --username AWS \
  --password-stdin ${ECR_URL}
```
Now we tag our docker image with a special tag, and then push it to ECR:
```bash
REMOTE_IMAGE_TAG="${ECR_URL}/churn-prediction-lambda:v1"

docker build -t churn-prediction-lambda .
docker tag churn-prediction-lambda ${REMOTE_IMAGE_TAG}
docker push ${REMOTE_IMAGE_TAG}
```

### AWS Lambda: TensorFlow Models
To get the model converted to onnx
```bash
wget https://github.com/DataTalksClub/machine-learning-zoomcamp/releases/download/dl-models/clothing-model-new.onnx
```
To install onnx
```bash
pip install onnxruntime
```
To insally keras-image-helper
```bash
pip install keras-image-helper
```
Build and run:
```bash
docker build -t clothing-lambda-keras .
docker run -it --rm -p 8080:8080 clothing-lambda-keras
```
