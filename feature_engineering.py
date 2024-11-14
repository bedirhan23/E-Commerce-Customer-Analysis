# feature_engineering.py

import pandas as pd


def add_recency_satisfaction(data):
    def recent_satisfaction(row):
        if row['Satisfaction Level'] >= 3 and row['Days Since Last Purchase'] < 30:
            return "High Recency Satisfaction"
        elif row['Satisfaction Level'] <= 2 and row['Days Since Last Purchase'] >= 30:
            return "Low Recency Satisfaction"
        else:
            return "Moderate Recency Satisfaction"

    data['Recent_Satisfaction'] = data.apply(recent_satisfaction, axis=1)
    return data


def add_satisfaction_dropoff(data):
    def satisfaction_dropoff(row):
        if row['Satisfaction Level'] <= 2 and row['Days Since Last Purchase'] > 60:
            return "High Dropoff"
        elif row['Satisfaction Level'] <= 2 and row['Days Since Last Purchase'] <= 60:
            return "Moderate Dropoff"
        else:
            return "Low Dropoff"

    data['Satisfaction_Dropoff'] = data.apply(satisfaction_dropoff, axis=1)
    return data


def add_high_spender_discount_feature(data):
    # Yüksek harcama yapan ve indirim alan müşteri özellikleri
    data['High_Spender'] = data['Total Spend'] > data['Total Spend'].mean()
    data['Discount_and_High_Spend'] = (data['High_Spender'] & data['Discount Applied'])
    return data


def add_purchase_frequency(data):
    # Müşterinin alışveriş sıklığını analiz etmek için yeni bir özellik
    def purchase_frequency(row):
        if row['Days Since Last Purchase'] <= 30:
            return 'Frequent Buyer'
        elif row['Days Since Last Purchase'] <= 90:
            return 'Occasional Buyer'
        else:
            return 'Rare Buyer'

    data['Purchase Frequency'] = data.apply(purchase_frequency, axis=1)
    return data


def add_loyalty_score(data):
    # Müşteri bağlılık puanı, harcama miktarına ve memnuniyet düzeyine göre oluşturulmuş bir özellik
    data['Loyalty Score'] = data['Total Spend'] * data['Satisfaction Level']
    return data


def feature_engineering(data):
    data = add_recency_satisfaction(data)
    data = add_satisfaction_dropoff(data)
    data = add_high_spender_discount_feature(data)
    data = add_purchase_frequency(data)
    data = add_loyalty_score(data)
    return data

def check_features(data):
    # 'Discount_and_High_Spend' ve 'Purchase Frequency' benzersiz değerleri ve 'Satisfaction Level' ortalamaları
    print("Discount_and_High_Spend Özeti:")
    print(data.groupby('Discount_and_High_Spend')['Satisfaction Level'].mean())
    print("\nPurchase Frequency Özeti:")
    print(data.groupby('Purchase Frequency')['Satisfaction Level'].mean())

# # Özellik özetini çağır
# check_features(data)
