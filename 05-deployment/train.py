#!/usr/bin/env python
# coding: utf-8
import pickle

import pandas as pd
import numpy as np
import sklearn
from sklearn.pipeline import make_pipeline


print(f'pandas=={pd.__version__}')
print(f'numpy=={np.__version__}')
print(f'sklearn=={sklearn.__version__}')



from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression



data_url = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-03-churn-prediction/WA_Fn-UseC_-Telco-Customer-Churn.csv'

def load_data(data_url):
    df = pd.read_csv(data_url)

    df.columns = df.columns.str.lower().str.replace(' ', '_')

    categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)

    for c in categorical_columns:
        df[c] = df[c].str.lower().str.replace(' ', '_')

    df.totalcharges = pd.to_numeric(df.totalcharges, errors='coerce')
    df.totalcharges = df.totalcharges.fillna(0)

    df.churn = (df.churn == 'yes').astype(int)

    return df


def train_model(df):


    numerical = ['tenure', 'monthlycharges', 'totalcharges']

    categorical = [
        'gender',
        'seniorcitizen',
        'partner',
        'dependents',
        'phoneservice',
        'multiplelines',
        'internetservice',
        'onlinesecurity',
        'onlinebackup',
        'deviceprotection',
        'techsupport',
        'streamingtv',
        'streamingmovies',
        'contract',
        'paperlessbilling',
        'paymentmethod',
    ]

    y_train = df.churn

    train_dict = df[categorical + numerical].to_dict(orient='records')

    pipeline = make_pipeline(
    DictVectorizer(),
    LogisticRegression(solver='liblinear')
   )

    pipeline.fit(train_dict, y_train)

    return pipeline


def save_model(pipeline, output_file):
    with open(output_file, 'wb') as f_out:
        pickle.dump(pipeline, f_out)

data_url = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-03-churn-prediction/WA_Fn-UseC_-Telco-Customer-Churn.csv'

df = load_data(data_url)
pipeline = train_model(df)
save_model(pipeline, 'model.bin')

print('Model saved to model.bin')

# datapoint = {
#     'gender': 'male',
#     'seniorcitizen': 0,
#     'partner': 'no',
#     'dependents': 'no',
#     'phoneservice': 'no',
#     'multiplelines': 'no_phone_service',
#     'internetservice': 'dsl',
#     'onlinesecurity': 'no',
#     'onlinebackup': 'yes',
#     'deviceprotection': 'no',
#     'techsupport': 'no',
#     'streamingtv': 'no',
#     'streamingmovies': 'no',
#     'contract': 'month-to-month',
#     'paperlessbilling': 'yes',
#     'paymentmethod': 'electronic_check',
#     'tenure': 6,
#     'monthlycharges': 29.85,
#     'totalcharges': 129.85
# }


# # In[9]:




# # In[22]:


# pipeline.predict_proba(datapoint)[0, 1]


# # In[23]:





# # In[24]:


# with open('model.bin', 'rb') as f_in:
#     pipeline = pickle.load(f_in)


# # In[25]:


# pipeline.predict_proba(datapoint)[0, 1]


# # In[ ]:




