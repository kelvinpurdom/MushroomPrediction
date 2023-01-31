# import packages
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.compose import make_column_selector
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import joblib
from sklearn.metrics import accuracy_score

# random seed
seed = 42

# Import the dataset
df = pd.read_csv('raw_data/secondary_data.csv', sep=";", low_memory=False)

# Shuffle the rows of the dataset using a random seed
df.sample(frac=1, random_state=seed)

# Drop the columns that are not needed
drop_columns = ['gill-spacing', 'stem-root',
                'stem-surface', 'veil-type',
                'veil-color', 'spore-print-color',
                ]
df.drop(columns=drop_columns, inplace=True)

# Split the dataset into feature matrix X and target vector y
X = df.drop(columns='class')
y = df['class']

# Split the data into training and testing sets using stratified sampling
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=seed, stratify=y)

# Define the preprocessor to transform the data
preprocessor = ColumnTransformer([
    ('num_encoder', MinMaxScaler(), make_column_selector(dtype_include="float64")),
    ('cat_encoder', OneHotEncoder(handle_unknown='ignore', sparse=False), make_column_selector(dtype_include="object"))
    ],remainder='passthrough')

# Define the pipeline to process the data and train the Random Forest model
pipe = Pipeline([
    ('preprocessing', preprocessor),
    ('RandomForestClassifier', RandomForestClassifier(n_estimators=1000,
                                                      criterion='gini',
                                                      max_depth= 30,
                                                      random_state=seed)),
    ])

# Fit the pipeline on the training data
pipe.fit(X_train,y_train)

# Make predictions on the test set
y_pred = pipe.predict(X_test)

# calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Save the pipeline to a .sav
joblib.dump(pipe, 'pipe_rf_model.sav')
