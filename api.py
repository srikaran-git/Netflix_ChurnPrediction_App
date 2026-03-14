from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel

# Load model and encoder safely
try:
    artifacts = joblib.load("model.pkl")
    model = artifacts.get('model')
    encoder = artifacts.get('encoder')
except Exception as e:
    model = None
    encoder = None
app = FastAPI()

class NetflixInput(BaseModel):
    age: int
    salary_k: float
    tenure_years: float
    number_of_logins: int
    complaints: int
    engagement_score: float
    Years_from_signup: float
    days_from_last_active_day: int
    region: str
    device_type: str

@app.get("/")
def home():
    if model is None:
        return {"message": "ML API is running but model.pkl is not found. Please run the notebook and save the model."}
    return {"message": "ML API is running and model is loaded successfully."}

@app.post("/predict")
def predict(data: NetflixInput):
    if model is None or encoder is None:
        return {"error": "Model or encoder not loaded. Please save them from the notebook first."}

    # 1. Create DataFrame for numerical features
    numeric_cols = ['age', 'salary_k', 'tenure_years', 'number_of_logins',
                    'complaints', 'engagement_score', 'Years_from_signup', 'days_from_last_active_day']
    
    num_df = pd.DataFrame([{
        'age': data.age,
        'salary_k': data.salary_k,
        'tenure_years': data.tenure_years,
        'number_of_logins': data.number_of_logins,
        'complaints': data.complaints,
        'engagement_score': data.engagement_score,
        'Years_from_signup': data.Years_from_signup,
        'days_from_last_active_day': data.days_from_last_active_day
    }])
    
    # 2. Process categorical features just like in the notebook
    cat_df = pd.DataFrame([{
        'region': data.region,
        'device_type': data.device_type
    }])
    
    encoded_cat = encoder.transform(cat_df)
    encoded_cat_df = pd.DataFrame(
        encoded_cat.toarray(), 
        columns=encoder.get_feature_names_out()
    )
    
    # 3. Combine them
    X_input = pd.concat([num_df, encoded_cat_df], axis=1)
    
    # 4. Predict
    prediction = int(model.predict(X_input)[0])
    
    return {
        "churn_prediction": prediction,
        "churn_likelihood": bool(prediction == 1)
    }