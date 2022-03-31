import pandas as pd
from pycaret.classification import load_model, predict_model
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class Variables(BaseModel):
    BMI:float
    Age: int
    Income: int
    PhysHlth: int
    Education: int
    GenHlth: int
    MentHlth: int
    HighBP: int
    Fruits: int
    Smoker: int

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)                                                                     

@app.post("/predict")
async def model(data:Variables):   
    rf_model = load_model("model/RF_model_diabetes")
    columns = ['BMI','Age','Income','PhysHlth', 'Education', 'GenHlth', 'MentHlth', 'HighBP', 'Fruits', 'Smoker']

    data = data.dict()
    input_values = [[
        data["BMI"],
        data["Age"],
        data["Income"],
        data["PhysHlth"],
        data["Education"],
        data["GenHlth"],
        data["MentHlth"],
        data["HighBP"],
        data["Fruits"],
        data["Smoker"]]]
        
    input_df = pd.DataFrame(data=input_values,columns=columns)

    predict = predict_model(rf_model,data=input_df)

    predict_value = int(predict['Label'][0])
    score_value = float(predict['Score'][0])

    return {"predict": predict_value,"score":score_value}
