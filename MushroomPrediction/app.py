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
    if cap_shape == 'Convex':
        cap_shape = 'x'
    elif cap_shape == 'Flat':
        cap_shape = 'f'
    elif cap_shape == 'Sunken':
        cap_shape = 's'
    elif cap_shape == 'Bell':
        cap_shape = 'b'
    elif cap_shape == 'Other':
        cap_shape = 'o'
    elif cap_shape == 'Sepherical':
        cap_shape = 'p'
    elif cap_shape == 'Conical':
        cap_shape = 'c'

    if cap_surface == 'Sticky':
        cap_surface = 't'
    elif cap_surface == 'Smooth':
        cap_surface = 's'
    elif cap_surface == 'Scaley':
        cap_surface = 'y'
    elif cap_surface == 'Shiney':
        cap_surface = 'h'
    elif cap_surface == 'Grooves':
        cap_surface = 'g'
    elif cap_surface == 'Convex':
        cap_surface = 'd'
    elif cap_surface == 'Fleshy':
        cap_surface = 'e'
    elif cap_surface == 'Silky':
        cap_surface = 'k'
    elif cap_surface == 'Fibrous':
        cap_surface = 'i'
    elif cap_surface == 'Wrinkled':
        cap_surface = 'w'
    elif cap_surface == 'leathery':
        cap_surface = 'l'

    if cap_color == 'Brown':
        cap_color = 'n'
    elif cap_color == 'Yellow':
        cap_color = 'y'
    elif cap_color == 'White':
        cap_color = 'w'
    elif cap_color == 'Grey':
        cap_color = 'g'
    elif cap_color == 'Red':
        cap_color = 'e'
    elif cap_color == 'Orange':
        cap_color = 'o'
    elif cap_color == 'Green':
        cap_color = 'r'
    elif cap_color == 'Purple':
        cap_color = 'u'
    elif cap_color == 'Pink':
        cap_color = 'p'
    elif cap_color == 'Black':
        cap_color = 'k'
    elif cap_color == 'Blue':
        cap_color = 'l'
    elif cap_color == 'Buff':
        cap_color = 'b'

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

cap_shape = st.selectbox('Cap Shape:', ['Convex', 'Flat', 'Sunken', 'Bell', 'Other', 'Spherical', 'Conical'])

cap_surface = st.selectbox('Cap Surface:', ['t', 's', 'y', 'h', 'g', 'd', 'e', 'k', 'i', 'w', 'l'])

cap_color = st.selectbox('Cap Color:', ['n', 'y', 'w', 'g', 'e', 'o', 'r', 'p', 'k', 'b', 'l'])

does_bruise_or_bleed = st.selectbox('Does Bruise or Bleed:', ['f', 't'])

gill_attachment = st.selectbox('Gill Attachment:', ['a', 'd', 'x', 'p', 'e', 's', 'f'])

gill_color = st.selectbox('Gill Color:', ['a', 'd', 'x', 'p', 'e', 's', 'f'])

stem_height = st.number_input('Stem Height:', min_value=0.0, max_value=34.0, value=1.0)

stem_width = st.number_input('Stem Width:', min_value=0.0, max_value=34.0, value=1.0)

stem_color = st.selectbox('Stem Color:', ['w', 'n', 'y', 'g', 'o', 'e', 'u', 'f', 'p', 'k', 'r', 'l', 'b'])

has_ring = st.selectbox('has-ring:', ['f', 't'])

ring_type = st.selectbox('Ring Type:', ['f', 'e', 'z', 'l', 'r', 'p', 'g', 'm'])

habitat = st.selectbox('Habitat:', ['d', 'g', 'l', 'm', 'h', 'p', 'w', 'u'])

season = st.selectbox('Season:', ['a', 'u', 'w', 's'])

if st.button('Predict if Poisonous'):
    poison = predict(cap_diameter, cap_shape, cap_surface,
                    cap_color, does_bruise_or_bleed,gill_attachment,
                    gill_color,stem_height,stem_width, stem_color,
                    has_ring,ring_type, habitat, season)
    st.success(f'The Mushroom is {poison[0]:.2f}')
