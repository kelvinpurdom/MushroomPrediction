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

    if does_bruise_or_bleed == 'False':
        does_bruise_or_bleed = 'f'
    elif does_bruise_or_bleed == 'True':
        does_bruise_or_bleed = 't'

    if gill_attachment == 'Adnate':
        gill_attachment = 'a'
    elif gill_attachment == 'Adnexed':
        gill_attachment = 'x'
    elif gill_attachment == 'Decurrent':
        gill_attachment = 'd'
    elif gill_attachment == 'Free':
        gill_attachment = 'e'
    elif gill_attachment == 'Sinuate':
        gill_attachment = 's'
    elif gill_attachment == 'Pores':
        gill_attachment = 'p'
    elif gill_attachment == 'None':
        gill_attachment = 'f'

    if gill_color == 'Brown':
        gill_color = 'n'
    elif cap_color == 'Yellow':
        gill_color = 'y'
    elif gill_color == 'White':
        gill_color = 'w'
    elif gill_color == 'Grey':
        gill_color = 'g'
    elif gill_color == 'Red':
        gill_color = 'e'
    elif gill_color == 'Orange':
        gill_color = 'o'
    elif gill_color == 'Green':
        gill_color = 'r'
    elif gill_color == 'Purple':
        gill_color = 'u'
    elif gill_color == 'Pink':
        gill_color = 'p'
    elif gill_color == 'Black':
        gill_color = 'k'
    elif gill_color == 'Blue':
        gill_color = 'l'
    elif gill_color == 'Buff':
        gill_color = 'b'
    elif gill_color == 'None':
        gill_color = 'f'

    if has_ring == 'False':
        has_ring = 'f'
    elif has_ring == 'True':
        has_ring = 't'


    if ring_type == 'Evanescent':
        ring_type = 'e'
    elif ring_type == 'Flaring':
        ring_type = 'r'
    elif ring_type == 'Grooved':
        ring_type = 'g'
    elif ring_type == 'Pendant':
        ring_type = 'p'
    elif ring_type == 'Zone':
        ring_type = 'z'
    elif ring_type == 'Movable':
        ring_type = 'm'
    elif ring_type == 'None':
        ring_type = 'f'

    if habitat == 'Grasses':
        habitat = 'g'
    elif habitat == 'Leaves':
        habitat = 'l'
    elif habitat == 'Meadows':
        habitat = 'm'
    elif habitat == 'Paths':
        habitat = 'p'
    elif habitat == 'Heaths':
        habitat = 'h'
    elif habitat == 'Urban':
        habitat = 'u'
    elif habitat == 'Waste':
        habitat = 'w'
    elif habitat == 'Woods':
        habitat = 'd'

    if season == 'Spring':
        season = 's'
    elif season == 'Summer':
        season = 'u'
    elif season == 'Autumn':
        season = 'a'
    elif season == 'Winter':
        season = 'w'







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

gill_color = st.selectbox('Gill Color:', ['n', 'y', 'w', 'g', 'e', 'o', 'r', 'p', 'k', 'b', 'l'])

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
