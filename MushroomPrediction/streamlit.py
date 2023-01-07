from sklearn.ensemble import RandomForestClassifier
import streamlit as st
import pandas as pd
from sklearn.pipeline import Pipeline

pipe = Pipeline()
pipe.load_model('rf_model.json')
