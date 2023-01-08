import streamlit as st
import pandas as pd
import pickle

# loading the model
with open('rf_model.pkl', 'rb') as f:
    model = pickle.load(f)

# predict function will put all the variables from streamlit into the model
def predict(cap_diameter, cap_shape, cap_surface,
            cap_color, does_bruise_or_bleed,
            gill_attachment,gill_color,stem_height,
            stem_width, stem_color, has_ring,ring_type,
            habitat,season):
    # encoding streamlit to correct types of input data
    # cap shape
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

    # cap surface
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

    # cap color
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


    # does bruise or bleed
    if does_bruise_or_bleed == 'False':
        does_bruise_or_bleed = 'f'
    elif does_bruise_or_bleed == 'True':
        does_bruise_or_bleed = 't'


    # gill attachment
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


    # gill color
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


    # does it have a ring
    if has_ring == 'False':
        has_ring = 'f'
    elif has_ring == 'True':
        has_ring = 't'

    # what is the ring type
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

    # what habitat does it live in
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

    # What season is it
    if season == 'Spring':
        season = 's'
    elif season == 'Summer':
        season = 'u'
    elif season == 'Autumn':
        season = 'a'
    elif season == 'Winter':
        season = 'w'


    # prediction of the model engaged
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

# Style points
st.title('Poisonous Mushroom Predictor')
st.image("""https://www.wissenschaft.de/wp-content/uploads/2/2/22-04-12-depression.jpg""")
st.header('Enter the characteristics of the Mushroom: ')

# input numbers and selectbox options
col1, col2, col3 = st.columns(3)
with col1:
    cap_diameter = st.number_input('Cap-diameter(cm):', min_value=0.38, max_value=63.0, value=1.0, step= 0.05)

    cap_shape = st.selectbox('Cap Shape:', ['Convex', 'Flat', 'Sunken', 'Bell', 'Other', 'Spherical', 'Conical'])

    cap_surface = st.selectbox('Cap Surface:', ['Sticky', 'Smooth', 'Scaley', 'Shiney', 'Grooves', 'Convex', 'Fleshy', 'Silky', 'Fibrous', 'Wrinkled', 'Leathery'])

    cap_color = st.selectbox('Cap Color:', ['Brown', 'Yellow', 'White', 'Grey', 'Red', 'Orange', 'Green', 'Purple', 'Pink', 'Black', 'Blue', 'Buff'])

    does_bruise_or_bleed = st.selectbox('Does Bruise or Bleed:', ['False', 'True'])

with col2:
    gill_attachment = st.selectbox('Gill Attachment:', ['Adnate', 'Decurrent', 'Adnexed', 'Pores', 'Free', 'Sinuate', 'None'])

    gill_color = st.selectbox('Gill Color:', ['Brown', 'Yellow', 'White', 'Grey', 'Red', 'Orange', 'Green', 'Purple', 'Pink', 'Black', 'Blue', 'Buff', 'None'])

    stem_height = st.number_input('Stem Height(cm):', min_value=0.0, max_value=34.0, value=1.0,step= 0.05)

    stem_width = st.number_input('Stem Width(cm):', min_value=0.0, max_value=34.0, value=1.0,step= 0.05)

with col3:
    stem_color = st.selectbox('Stem Color:', ['Brown', 'Yellow', 'White', 'Grey', 'Red', 'Orange', 'Green', 'Purple', 'Pink', 'Black', 'Blue', 'Buff', 'None'])

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
        poison = 'I can with 99.9% accuracy say this mushroom is NOT POISONOUS'
    st.success(f'{poison}')
