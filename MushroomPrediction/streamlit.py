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

st.title('Poisonous Mushroom Predictor')
st.image("""https://www.thestreet.com/.image/ar_4:3%2Cc_fill%2Ccs_srgb%2Cq_auto:good%2Cw_1200/MTY4NjUwNDYyNTYzNDExNTkx/why-dominion-diamonds-second-trip-to-the-block-may-be-different.png""")
st.header('Enter the characteristics of the Mushroom: ')

cap_diameter = st.number_input('Cap-diameter:', min_value=0.38, max_value=63.0, value=1.0)
cap_shape = st.selectbox('Cap-shape', ['x', 'f', 's', 'b', 'o', 'p', 'c'])
cap_surface = st.selectbox('Cap-surface', ['t', 's', 'y', 'h', 'g', 'd', 'e', 'k', 'i', 'w', 'l'])
cap_color = st.selectbox('Cap-color', ['n', 'y', 'w', 'g', 'e', 'o', 'r', 'p', 'k', 'b', 'l'])
does_bruise_or_bleed = st.selectbox('does-bruise-or-bleed', ['f', 't'])
gill_attachment =
