#  Netflix Churn Prediction App

An end-to-end **Machine Learning project** that predicts whether a Netflix user is likely to churn or not.
This project integrates **model training, API development, and web app deployment** using modern tools.

---

##  Live Demo

👉 https://netflixchurnpredictionapp-srikaran.streamlit.app/

---

##  Project Overview

Customer churn is a critical problem for subscription-based platforms like Netflix.
This project uses Machine Learning techniques to **analyze user behavior and predict churn**, helping businesses take proactive retention measures.

---

##  Tech Stack

###  Machine Learning

* XGBoost Classifier
* SMOTE (for handling class imbalance)
* Scikit-learn

###  Backend

* FastAPI
* Uvicorn

###  Frontend

* Streamlit

###  Other Tools

* Pandas, NumPy
* Jupyter Notebook

---

## 📂 Project Structure

```
Netflix-Churn-Prediction/
│
├── app.py               # Streamlit frontend
├── api.py               # FastAPI backend
├── model.pkl            # Trained ML model
├── data.csv             # Dataset
├── notebook.ipynb       # Model training & analysis
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## ⚙️ How It Works

1. **Data Preprocessing**

   * Cleaned and transformed raw data
   * Handled missing values
   * Applied feature engineering

2. **Handling Class Imbalance**

   * Used **SMOTE** to balance churn vs non-churn classes

3. **Model Training**

   * Trained using **XGBoost Classifier**
   * Optimized for better prediction performance

4. **Model Deployment**

   * Backend API built using FastAPI
   * Served using Uvicorn
   * Frontend built with Streamlit for user interaction

---

##  Model Performance

* Evaluation metrics (accuracy, precision, recall, etc.) are included in the Jupyter Notebook
* The model is optimized to handle imbalanced data effectively

---

##  How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/srikaran-git/Netflix_ChurnPrediction_App.git
cd Netflix-Churn-Prediction
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run FastAPI Server

```bash
uvicorn api:app --reload
```

### 5. Run Streamlit App

```bash
streamlit run app.py
```

---

##  Key Features

* End-to-end ML pipeline
* Handles class imbalance using SMOTE
* API-based architecture (FastAPI + Uvicorn)
* Interactive UI with Streamlit
* Real-time predictions

---

## 📊 Dataset

* Dataset used for training is included (`getflix_synthetic_dataset_v2.csv`)
* Additional details and preprocessing steps are available in the notebook

---


## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

---
