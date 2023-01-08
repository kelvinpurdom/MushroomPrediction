from sklearn.ensemble import RandomForestClassifier
import streamlit as st
import pandas as pd
import pickle
from sklearn.pipeline import Pipeline

with open('../notebooks/rf_model.pkl', 'rb') as f:
    model = pickle.load(f)

@st.cache

def predict(cap_diameter, cap_shape, cap_surface,
            cap_color, does_bruise_or_bleed,
            gill_attachment,gill_color,stem_height,
            stem_width, stem_color, has_ring,ring_type,
            habitat,season)



prediction = model.predict(pd.DataFrame([[cap_diameter, cap_shape, cap_surface,
            cap_color, does_bruise_or_bleed,
            gill_attachment,gill_color,stem_height,
            stem_width, stem_color, has_ring,ring_type,
            habitat,season]],
                                        columns=['cap-diameter', 'cap-shape', 'cap-surface',
                                                 'cap-color', 'does-bruise-or-bleed',
                                                 'gill-attachment', 'gill-color','stem-height',
                                                 'stem-width', 'stem-color', 'has-ring','ring-type',
                                                 'habitat','season']))
return prediction
