# import packages
import streamlit as st
import pandas as pd
from prediction import predict
import webbrowser

# set tab button
st.set_page_config(page_title='Mushroom Prediction')

# remove menu and footer from streamlit
hide_default_format = """
       <style>

       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# Set the title of the page
st.title('The Poisonous Mushroom Predictor')
st.subheader('Created by Kelvin Purdom')
st.markdown("""Using the Random Forest Classifier
            and preprocessing tools, I have built
            a Machine Learning Model that can predict
            with 99.9% accuracy, if a mushroom is
            poisonous using these variables below. Try it out!""")

url = 'https://github.com/kelvinpurdom'
if st.button('Kelvins Github'):
    webbrowser.open_new_tab(url)
st.image("""https://www.wissenschaft.de/wp-content/uploads/2/2/22-04-12-depression.jpg""")
st.markdown('Photo: Shutterstock')
st.subheader("Enter the Characteristics of the Mushroom:")

# Create three columns on the page
col1, col2, col3 = st.columns(3)

with col1:
    cap_diameter = st.number_input('Cap-diameter(cm):', min_value=0.0, max_value=64.0, value=1.0, step= 1.0)
    cap_surface = st.selectbox('Cap Surface:', ['Sticky', 'Smooth', 'Scaley', 'Shiney', 'Grooves', 'Convex', 'Fleshy', 'Silky', 'Fibrous', 'Wrinkled', 'Leathery'])
    cap_color = st.selectbox('Cap Colour:', ['Brown', 'Yellow', 'White', 'Grey', 'Red', 'Orange', 'Green', 'Purple', 'Pink', 'Black', 'Blue', 'Buff'])
    does_bruise_or_bleed = st.selectbox('Does Bruise or Bleed:', ['False', 'True'])
    cap_shape = st.selectbox('Cap Shape:', ['Convex', 'Flat', 'Sunken', 'Bell Shaped', 'Other', 'Spherical', 'Conical'])
    st.image("""https://i0.wp.com/midwestmycology.org/wp-content/uploads/2019/06/mushroom-cap-shapes.jpg?fit=900%2C178&ssl=1""")
with col2:

    st.markdown('')
    gill_color = st.selectbox('Gill Colour:', ['Brown', 'Yellow', 'White', 'Grey', 'Red', 'Orange', 'Green', 'Purple', 'Pink', 'Black', 'Blue', 'Buff', 'None'])
    st.markdown('')
    stem_height = st.number_input('Stem Height(cm):', min_value=0.0, max_value=34.0, value=1.0,step= 1.0)
    st.markdown('')
    stem_width = st.number_input('Stem Width(cm):', min_value=0.0, max_value=34.0, value=1.0,step= 1.0)
    st.markdown('')
    gill_attachment = st.selectbox('Gill Attachment:', ['Adnate', 'Descending', 'Adnexed', 'Notched', 'Free', 'Seceding', 'None'])
    st.markdown('')
    st.markdown('')
    st.image("""https://biolwww.usask.ca/fungi/graphics/glossary_pictures/glossary_pic19""")
with col3:

    stem_color = st.selectbox('Stem Colour:', ['Brown', 'Yellow', 'White', 'Grey', 'Red', 'Orange', 'Green', 'Purple', 'Pink', 'Black', 'Blue', 'Buff', 'None'])
    has_ring = st.selectbox('Has a Ring:', ['False', 'True'])
    habitat = st.selectbox('Habitat:', ['Woods', 'Grasses', 'Leaves', 'Meadows', 'Heaths', 'Paths', 'Waste', 'Urban'])
    season = st.selectbox('Season:', ['Spring', 'Summer', 'Winter', 'Summer'])
    ring_type = st.selectbox('Ring Type:', ['Sheathing', 'Grooved', 'Pendant', 'Ring Zone', 'Cobwebby', 'None'])
    st.image("""https://datascienceplus.com/wp-content/uploads/2018/02/mushroom-ring-type.jpg""")

# Translate input buttons into the expected values for the model

# cap shape
if cap_shape == 'Convex':
    cap_shape = 'x'
elif cap_shape == 'Flat':
    cap_shape = 'f'
elif cap_shape == 'Sunken':
    cap_shape = 's'
elif cap_shape == 'Bell Shaped':
    cap_shape = 'b'
elif cap_shape == 'Other':
    cap_shape = 'o'
elif cap_shape == 'Sepherical':
    cap_shape = 'p'
else:
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
else:
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
else:
    cap_color = 'b'

# does bruise or bleed
if does_bruise_or_bleed == 'False':
    does_bruise_or_bleed = 'f'
else:
    does_bruise_or_bleed = 't'

# gill attachment
if gill_attachment == 'Adnate':
    gill_attachment = 'a'
elif gill_attachment == 'Adnexed':
    gill_attachment = 'x'
elif gill_attachment == 'Decsending':
    gill_attachment = 'd'
elif gill_attachment == 'Free':
    gill_attachment = 'e'
elif gill_attachment == 'Seceding':
    gill_attachment = 's'
elif gill_attachment == 'Notched':
    gill_attachment = 'p'
else:
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
else:
    gill_color = 'f'

# gill color
if stem_color == 'Brown':
    stem_color = 'n'
elif stem_color == 'Yellow':
    stem_color = 'y'
elif stem_color == 'White':
    stem_color = 'w'
elif stem_color == 'Grey':
    stem_color = 'g'
elif stem_color == 'Red':
    stem_color = 'e'
elif stem_color == 'Orange':
    stem_color = 'o'
elif stem_color == 'Green':
    stem_color = 'r'
elif stem_color == 'Purple':
    stem_color = 'u'
elif stem_color == 'Pink':
    stem_color = 'p'
elif stem_color == 'Black':
    stem_color = 'k'
elif stem_color == 'Blue':
    stem_color = 'l'
elif stem_color == 'Buff':
    stem_color = 'b'
else:
    stem_color = 'f'


# does it have a ring
if has_ring == 'False':
    has_ring = 'f'
else:
    has_ring = 't'

# what is the ring type
if ring_type == 'Sheathing':
    ring_type = 'e'
elif ring_type == 'Flaring':
    ring_type = 'r'
elif ring_type == 'Grooved':
    ring_type = 'g'
elif ring_type == 'Pendant':
    ring_type = 'p'
elif ring_type == 'Ring Zone':
    ring_type = 'z'
elif ring_type == 'Cobwebby':
    ring_type = 'm'
else:
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
else:
    habitat = 'd'

# What season is it
if season == 'Spring':
    season = 's'
elif season == 'Summer':
    season = 'u'
elif season == 'Autumn':
    season = 'a'
elif season== 'Winter':
    season = 'w'


# streamlit button to activate predict function
if st.button('Is This Mushroom Poisonous? '):
    result = predict(pd.DataFrame([[cap_diameter, cap_shape, cap_surface,
                                    cap_color, does_bruise_or_bleed,
                                    gill_attachment,gill_color,stem_height,
                                    stem_width, stem_color, has_ring, ring_type,
                                    habitat,season]],
                                  columns=['cap-diameter', 'cap-shape', 'cap-surface',
                                           'cap-color', 'does-bruise-or-bleed',
                                           'gill-attachment', 'gill-color','stem-height',
                                           'stem-width', 'stem-color', 'has-ring','ring-type',
                                           'habitat','season'
                                           ]))

    if result[0] == 'p':
        # if Mushroom is predicted as poisonous
        st.header('YES, Be Careful, I am very, very, very sure that this Mushroom contains Poison')
        st.image("""https://www.udiscovermusic.com/wp-content/uploads/2020/10/Poison-GettyImages-1189389370.jpg""")
        st.markdown('Photo: Ross Marino/Getty Images')

    elif result[0] == 'e':
        # if Mushroom is predicted as not poisonous
        st.header('NO, With 99.9% accuracy, I can say this mushroom does not contain Poison')
        st.image("""https://www.udiscovermusic.com/wp-content/uploads/2020/11/Mo%CC%88tley-Cru%CC%88e-GettyImages-1202277301.jpg""")
        st.markdown('Photo: Ross Marino/Getty Images')
