from sklearn.ensemble import RandomForestClassifier
import streamlit as st
import pandas as pd
import pickle
from sklearn.pipeline import Pipeline

with open('../notebooks/rf_model.pkl', 'rb') as f:
    model = pickle.load(f)
