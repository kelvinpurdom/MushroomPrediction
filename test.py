import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pickle

# Load the dataset
data = pd.read_csv('raw_data/secondary_data.csv')

# Define the features and target
X = data.drop(columns='class')
y = data['class']

# Define the categorical and numerical features
categorical_features = X.select_dtypes(include='object').columns
numerical_features = X.select_dtypes(exclude='object').columns

# Create a column transformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Create the pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier())
])



# Fit the pipeline to the training data
fitted_pipe = pipeline.fit(X, y)

filename = 'rf_model.pkl'
with open('./'+filename, 'wb') as file:
    pickle.dump(fitted_pipe, file)
