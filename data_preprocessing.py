# data_preprocessing.py

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder


def load_and_clean_data(file_path):
    data = pd.read_csv(file_path)
    data = data.dropna()  # Eksik verileri kaldırma
    return data


def preprocess_data(data):
    # Kategorik verileri sayısal değerlere dönüştürme
    # data['Gender'] = LabelEncoder().fit_transform(data['Gender'])
    # data['City'] = LabelEncoder().fit_transform(data['City'])
    # "satisfaction level" için encoding işlemi
    data['Satisfaction Level'] = data['Satisfaction Level'].map({
        'Unsatisfied': 1,
        'Neutral': 2,
        'Satisfied': 3
    })

    # Standartlaştırma
    # scaler = StandardScaler()
    # data[
    #     ['Age', 'Total Spend', 'Items Purchased', 'Average Rating', 'Days Since Last Purchase']] = scaler.fit_transform(
    #     data[['Age', 'Total Spend', 'Items Purchased', 'Average Rating', 'Days Since Last Purchase']]
    # )

    return data
