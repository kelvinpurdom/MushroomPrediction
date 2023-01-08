import streamlit as st
import pandas as pd
import pickle

with open('rf_model.pkl', 'rb') as f:
    model = pickle.load(f)


def predict(cap_diameter, cap_shape, cap_surface,
            cap_color, does_bruise_or_bleed,
            gill_attachment,gill_color,stem_height,
            stem_width, stem_color, has_ring,ring_type,
            habitat,season):

    prediction = model.predict(pd.DataFrame([[cap_diameter, cap_shape, cap_surface,
            cap_color, does_bruise_or_bleed,
            gill_attachment,gill_color,stem_height,
            stem_width, stem_color, has_ring, ring_type,
            habitat,season]],
                                        columns=['cap-diameter', 'cap-shape', 'cap-surface',
                                                 'cap-color', 'does-bruise-or-bleed',
                                                 'gill-attachment', 'gill-color','stem-height',
                                                 'stem-width', 'stem-color', 'has-ring','ring-type',
                                                 'habitat','season']))
    return prediction

st.title('Poisonous Mushroom Predictor')
st.image("""https://www.wissenschaft.de/wp-content/uploads/2/2/22-04-12-depression.jpg""")
st.header('Enter the characteristics of the Mushroom: ')

cap_diameter = st.number_input('Cap-diameter:', min_value=0.38, max_value=63.0, value=1.0)

cap_shape = st.selectbox('Cap-shape:', ['x', 'f', 's', 'b', 'o', 'p', 'c'])

cap_surface = st.selectbox('Cap-surface:', ['t', 's', 'y', 'h', 'g', 'd', 'e', 'k', 'i', 'w', 'l'])

cap_color = st.selectbox('Cap-color:', ['n', 'y', 'w', 'g', 'e', 'o', 'r', 'p', 'k', 'b', 'l'])

does_bruise_or_bleed = st.selectbox('does-bruise-or-bleed:', ['f', 't'])

gill_attachment = st.selectbox('Gill-attachment:', ['a', 'd', 'x', 'p', 'e', 's', 'f'])

gill_color = st.selectbox('Gill-color:', ['a', 'd', 'x', 'p', 'e', 's', 'f'])

stem_height = st.number_input('Stem-height:', min_value=0.0, max_value=34.0, value=1.0)

stem_width = st.number_input('Stem-width:', min_value=0.0, max_value=34.0, value=1.0)

stem_color = st.selectbox('Stem-color:', ['w', 'n', 'y', 'g', 'o', 'e', 'u', 'f', 'p', 'k', 'r', 'l', 'b'])

has_ring = st.selectbox('has-ring:', ['f', 't'])

ring_type = st.selectbox('has-ring:', ['f', 'e', 'z', 'l', 'r', 'p', 'g', 'm'])

habitat = st.selectbox('Habitat:', ['d', 'g', 'l', 'm', 'h', 'p', 'w', 'u'])

season = st.selectbox('Season:', ['a', 'u', 'w', 's'])

if st.button('Predict if Poisonous'):
    poison = predict(cap_diameter, cap_shape, cap_surface,
                    cap_color, does_bruise_or_bleed,gill_attachment,
                    gill_color,stem_height,stem_width, stem_color,
                    has_ring,ring_type, habitat, season)
    st.success(f'The Mushroom is {poison[0]:.2f}')
