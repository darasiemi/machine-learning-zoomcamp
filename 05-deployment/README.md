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

To install uv
```bash
pip install uv
```
### Environment management
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

### Docker

```bash
docker build -t predict-churn .
```

```bash
docker run -it --rm -p 9696:9696 predict-churn
```
