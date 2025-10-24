To turn a notebook to python code
```bash
jupyter nbconvert --to=script workshop-uv-fastapi.ipynb
mv workshop-uv-fastapi.py train.py
```

To install fastapi and uvicorn
```bash
pip install fastapi uvicorn
```

Proper way of running app
```bash
uvicorn predict:app --host 0.0.0.0 --port 9696 --reload
```

To send request
```bash
curl -X 'POST' 'http://localhost:9696/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 1,
    "monthlycharges": 29.85,
    "totalcharges": 29.85
}'
```


## Environment management
To install uv
```bash
pip install uv
```

To initialize uv
```bash
uv init
```

We don't need `main.py` so we remove it
```bash
rm main.py
```

To add modules
```bash
uv add scikit-learn fastapi uvicorn
```

We also have a development dependency we won't need in production
```bash
uv add --dev requests
```

If we want to run something in this virtual environment, simply prefix it with `uv run`:

```bash
uv run uvicorn predict:app --host 0.0.0.0 --port 9696 --reload
uv run python test.py
```

When you get a fresh copy of a project that already uses uv, you can install all the dependencies using the sync command:
```bash
uv sync
```

## Docker
To build image
```bash
docker build -t predict-churn .
```
To run docker container
```bash
docker run -it --rm -p 9696:9696 predict-churn
```

To test the endpoint
```bash
uv run python test.py 
```
## Model Deployment

### Architecture Overview
- The churn prediction service is packaged into a Docker container.
- This container is deployed to AWS Elastic Beanstalk.
- A marketing service sends requests to the Elastic Beanstalk environment.
- Elastic Beanstalk forwards these requests to the Docker container.
- The container processes the request and sends the response back to Elastic Beanstalk.
- Elastic Beanstalk relays the response to the requesting service.

### Scalability with Elastic Beanstalk (EB)
Elastic Beanstalk automatically scales the application based on traffic. If the churn prediction service receives a high volume of requests, EB automatically adds more instances of the service to handle the load without interruption (horizontal scaling). Similarly, when traffic decreases, EB scales down the number of instances to optimize resource utilization.

Install AWS EB CLI
```bash
 uv add --dev awsebcli
```

Initialize the EB environment:

```bash
uv run eb init -p docker -r eu-north-1 churn-serving
```
This command configures the EB environment with the following parameters:

- -p docker: Specifies the platform as Docker.
- -r eu-north-1: Sets the region to eu-north-1. You can choose a different region based on your account information.
- churn-serving: Defines the name of the environment.


To show the platform, run
```bash
uv run eb platform show
```

To create EB environment and deploy model
```bash
uv run eb create churn-serving-env
```
You will have to provide permissions

To terminate
```bash
uv run eb terminate churn-serving-env
```

