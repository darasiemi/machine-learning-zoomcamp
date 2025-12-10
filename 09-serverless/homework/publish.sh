ECR_URL=511900348839.dkr.ecr.eu-north-1.amazonaws.com
REPO_URL=${ECR_URL}/hair-prediction-lambda
REMOTE_IMAGE_TAG="${REPO_URL}:v2"

LOCAL_IMAGE=hair-prediction-lambda

aws ecr get-login-password \
  --region "eu-north-1" \
| docker login \
  --username AWS \
  --password-stdin ${ECR_URL}

docker build --no-cache -t ${LOCAL_IMAGE} .
docker tag ${LOCAL_IMAGE} ${REMOTE_IMAGE_TAG}
docker push ${REMOTE_IMAGE_TAG}

echo "Done"