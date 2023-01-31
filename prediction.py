# this python file, loads the trained model into streamlit.py

import joblib
def predict(data):
    rf = joblib.load('pipe_rf_model.sav')
    return rf.predict(data)
