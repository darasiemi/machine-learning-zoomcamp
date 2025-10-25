To initialize uv
```bash
uv init
```

To install scikit-learn
```bash
uv add scikit-learn==1.6.1
```

To install fastapi
```bash
uv add fastapi
```

To install requests
```bash
uv add --dev requests
```

To run the fastapi app
```bash
uv run predict.app
``or
```bash
uv run uvicorn predict:app --host 0.0.0.0 --port 9696 --reload
```

Got the schema of the code from model 4- 04-evaluation by running this code
```python
test_df = df[["lead_source",
    "number_of_courses_viewed",
    "annual_income"]]

for column in test_df.columns:
    if test_df[column].dtype == "object":
        print(test_df[column].value_counts())
    else:
        print(test_df[column].describe())
        
```

Build docker image
```bash
docker build --platform=linux/amd64 -t scoring-model .
```

Run docker image
```bash
docker run --platform=linux/amd64 -it --rm -p 9696:9696 scoring-model
```
