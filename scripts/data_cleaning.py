import pandas as pd
from sqlalchemy import create_engine

# Load the raw data
raw_data_path = '/Users/NP/Documents/telco-churn-project/data/raw_data.csv'
raw_data = pd.read_csv(raw_data_path)

# Handle missing values
raw_data['TotalCharges'] = pd.to_numeric(raw_data['TotalCharges'], errors='coerce')
raw_data.fillna(raw_data.median(), inplace=True)

# One-hot encode categorical variables
categorical_features = ['gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod']
data = pd.get_dummies(raw_data, columns=categorical_features, drop_first=True)

# Normalize numerical features
numerical_features = ['tenure', 'MonthlyCharges', 'TotalCharges']
data[numerical_features] = (data[numerical_features] - data[numerical_features].mean()) / data[numerical_features].std()

# Save cleaned data
cleaned_data_path = '/Users/NP/Documents/telco-churn-project/data/cleaned_data.csv'
data.to_csv(cleaned_data_path, index=False)

# Store cleaned data in SQL database
engine = create_engine('sqlite:///data/churn_data.db')
data.to_sql('churn', engine, index=False, if_exists='replace')

print("Data cleaning completed and saved to cleaned_data.csv and SQL database.")