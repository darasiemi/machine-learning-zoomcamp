import requests

url = 'http://localhost:9696/predict'

customer = {
    'gender': 'female',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'no',
    'phoneservice': 'no',
    'multiplelines': 'no_phone_service',
    'internetservice': 'dsl',
    'onlinesecurity': 'no',
    'onlinebackup': 'yes',
    'deviceprotection': 'no',
    'techsupport': 'no',
    'streamingtv': 'no',
    'streamingmovies': 'no',
    'contract': 'month-to-month',
    'paperlessbilling': 'yes',
    'paymentmethod': 'electronic_check',
    'tenure': 1,
    'monthlycharges': 29.85,
    'totalcharges': 29.85
}

try:
    response = requests.post(url, json=customer, timeout=10)   # <-- use json=, not data=
    response.raise_for_status()                               # raises if 4xx/5xx
    # Optionally ensure the server claims JSON
    if "application/json" not in response.headers.get("Content-Type",""):
        print("Non-JSON response:\n", response.text)
    else:
        predictions = response.json()
        if "churn" in predictions.keys():
            if predictions['churn']:
                print('customer is likely to churn, send promo')
            else:
                print('customer is not likely to churn')
        else:
            column = predictions["detail"][0]["loc"][1]
            msg = predictions["detail"][0]["msg"]
            input = predictions["detail"][0]["input"]
            print(f"wrong input for {column}, {msg}, got {input}")
except requests.HTTPError as e:
    print("HTTP error:", e, "Body:", response.text if 'r' in locals() else "")
except requests.exceptions.JSONDecodeError:
    print("Could not parse JSON. Raw body:\n", response.text)
except requests.RequestException as e:
    print("Request failed:", e)




# predictions = response.json()

# print(predictions)

