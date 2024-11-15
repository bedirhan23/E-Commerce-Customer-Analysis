import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder


def load_and_clean_data(file_path):
    data = pd.read_csv(file_path)
    data = data.dropna()  # Remove missing values
    return data


def preprocess_data(data):
    # Map 'Satisfaction Level' to numerical values
    data['Satisfaction Level'] = data['Satisfaction Level'].map({
        'Unsatisfied': 1,
        'Neutral': 2,
        'Satisfied': 3
    })

    # Check if 'Satisfaction_Dropoff' column exists before applying encoding
    if 'Satisfaction_Dropoff' in data.columns:
        label_encoder = LabelEncoder()
        data['Satisfaction_Dropoff'] = label_encoder.fit_transform(data['Satisfaction_Dropoff'])

    # Check if 'Purchase Frequency' column exists before encoding
    if 'Purchase Frequency' in data.columns:
        label_encoder = LabelEncoder()
        data['Purchase Frequency'] = label_encoder.fit_transform(data['Purchase Frequency'])

    # Check if 'Discount_and_High_Spend' column exists before encoding
    if 'Discount_and_High_Spend' in data.columns:
        label_encoder = LabelEncoder()
        data['Discount_and_High_Spend'] = label_encoder.fit_transform(data['Discount_and_High_Spend'])

    # Standardize numeric columns (optional, can be commented out)
    # scaler = StandardScaler()
    # data[['Age', 'Total Spend', 'Items Purchased', 'Days Since Last Purchase']] = scaler.fit_transform(
    #     data[['Age', 'Total Spend', 'Items Purchased', 'Days Since Last Purchase']]
    # )

    return data
