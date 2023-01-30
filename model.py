import streamlit as st
import pandas as pd
import pickle
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.compose import make_column_selector
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def pipe_pre():
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
    # Use pickle to save model for next usage.
    filename = 'rf_model.pkl'
    with open('./'+filename, 'wb') as file:
        pickle.dump(pipe, file)

    return pipe
