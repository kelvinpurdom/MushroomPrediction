import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

col1, col2, col3 = st.columns(3)
with col1:
    cap_diameter = st.number_input('Cap-diameter(cm):', min_value=0.0, max_value=64.0, value=1.0, step= 0.05)
    cap_shape = st.selectbox('Cap Shape:', ['Convex', 'Flat', 'Sunken', 'Bell', 'Other', 'Spherical', 'Conical'])
    cap_surface = st.selectbox('Cap Surface:', ['Sticky', 'Smooth', 'Scaley', 'Shiney', 'Grooves', 'Convex', 'Fleshy', 'Silky', 'Fibrous', 'Wrinkled', 'Leathery'])
    cap_color = st.selectbox('Cap Colour:', ['Brown', 'Yellow', 'White', 'Grey', 'Red', 'Orange', 'Green', 'Purple', 'Pink', 'Black', 'Blue', 'Buff'])
    does_bruise_or_bleed = st.selectbox('Does Bruise or Bleed:', ['False', 'True'])

with col2:
    gill_attachment = st.selectbox('Gill Attachment:', ['Adnate', 'Decurrent', 'Adnexed', 'Pores', 'Free', 'Sinuate', 'None'])
    gill_color = st.selectbox('Gill Colour:', ['Brown', 'Yellow', 'White', 'Grey', 'Red', 'Orange', 'Green', 'Purple', 'Pink', 'Black', 'Blue', 'Buff', 'None'])
    stem_height = st.number_input('Stem Height(cm):', min_value=0.0, max_value=34.0, value=1.0,step= 0.05)
    stem_width = st.number_input('Stem Width(cm):', min_value=0.0, max_value=34.0, value=1.0,step= 0.05)

with col3:
    stem_color = st.selectbox('Stem Colour:', ['Brown', 'Yellow', 'White', 'Grey', 'Red', 'Orange', 'Green', 'Purple', 'Pink', 'Black', 'Blue', 'Buff', 'None'])
    has_ring = st.selectbox('Has a Ring:', ['False', 'True'])
    ring_type = st.selectbox('Ring Type:', ['Evanescent', 'Flaring', 'Grooved', 'Pendant', 'Zone', 'Movable', 'None'])
    habitat = st.selectbox('Habitat:', ['Woods', 'Grasses', 'Leaves', 'Meadows', 'Heaths', 'Paths', 'Waste', 'Urban'])
    season = st.selectbox('Season:', ['Spring', 'Summer', 'Winter', 'Summer'])


#  streamlit button to activate predict function
if st.button('Predict if Poisonous'):
    poison = predict(cap_diameter, cap_shape, cap_surface,
                    cap_color, does_bruise_or_bleed,gill_attachment,
                    gill_color,stem_height,stem_width, stem_color,
                    has_ring,ring_type, habitat, season)

if poison[0] == 1:
    poison = 'Yes, I am very, very, very sure that this Mushroom IS POISONOUS'

else:
    poison = 'I can with 99.9','%',' accuracy say this mushroom is NOT POISONOUS'
st.success(f'{poison}')
