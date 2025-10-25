import os
import pickle
import uvicorn
from fastapi import FastAPI
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field

app = FastAPI( title = "lead-scoring-model")

model_file = os.getenv("MODEL_PATH", "/code/pipeline_v2.bin")

class Record(BaseModel):
    model_config = ConfigDict(extra="forbid")

    lead_source : Literal["organic_search", "social_media", "paid_ads" , "referral", "events"]
    number_of_courses_viewed: int = Field(..., ge=0)
    annual_income: float = Field(..., ge=0)


class PredictResponse(BaseModel):
    scoring_probability: float
    score: bool

def load_model(model_file):
    # model_file = "pipeline_v1.bin"

    with open(model_file, 'rb') as f_in:
        pipeline = pickle.load(f_in)
    
    return pipeline

@app.post("/predict")
def predict(record : Record) -> PredictResponse:
    pipeline = load_model(model_file)
    prob = pipeline.predict_proba(record.model_dump())[0, 1]

    return PredictResponse(
           scoring_probability = prob,
           score=prob >= 0.5 )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)


