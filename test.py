import streamlit as st
import pandas as pd
import pickle
import joblib
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.compose import make_column_selector
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

preprocessor = ColumnTransformer([
    ('num_encoder', MinMaxScaler(), make_column_selector(dtype_include="float64")),
    ('cat_encoder', OneHotEncoder(handle_unknown='ignore', sparse=False), make_column_selector(dtype_include="object"))
    ],remainder='passthrough')

pipe = Pipeline([
    ('preprocessing', preprocessor),
    ('RandomForestClassifier', RandomForestClassifier(n_estimators=1000,
                                                      criterion='gini',
                                                      max_depth= 30,
                                                      random_state=123)),
])

df = pd.read_csv('raw_data/secondary_data.csv', sep=";", low_memory=False)
drop_columns = ['gill-spacing', 'stem-root',
                'stem-surface', 'veil-type',
                'veil-color', 'spore-print-color',
                ]
df.drop(columns=drop_columns, inplace=True)

gender = {'p': 1,'e': 0}
df['class'] = [gender[item] for item in df['class']]

X = df.drop(columns='class')
y = df['class']


pipe.fit(X,y)

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
    if does_bruise_or_bleed == False:
        does_bruise_or_bleed = 'f'
    else:
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


    # does it have a ring
    if has_ring == False:
        has_ring = 'f'
    else:
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
    else:
        season = 'w'


    # prediction of the model engaged
    prediction = pipe.predict(pd.DataFrame([[cap_diameter, cap_shape, cap_surface,
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

print(predict(34,'Convex','Sticky', 'Yellow', False, 'Adnate', 'Brown', 56, 67, 'Brown', True , 'None', 'Waste', 'Summer'))
