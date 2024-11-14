# main.py

from data_preprocessing import load_and_clean_data, preprocess_data
from feature_engineering import feature_engineering
from visualization import (
    plot_city_distribution, plot_days_since_last_purchase,
    plot_satisfaction_vs_discount, plot_purchase_frequency_distribution,
    plot_loyalty_score_kde, plot_satisfaction_vs_loyalty,
    plot_purchase_frequency_vs_satisfaction
)
from A_B_Testing import membership_spendingABTesting, membership_satisfactionABTesting

# Veri Yükleme ve Temizleme
data = load_and_clean_data('data/E-commerce Customer Behavior - Sheet1.csv')
data = preprocess_data(data)

# Özellik Mühendisliği
data = feature_engineering(data)

def check_features(data):
    # 'Discount_and_High_Spend' ve 'Purchase Frequency' benzersiz değerleri ve 'Satisfaction Level' ortalamaları
    print("Discount_and_High_Spend Özeti:")
    print(data.groupby('Discount_and_High_Spend')['Satisfaction Level'].mean())
    print("\nPurchase Frequency Özeti:")
    print(data.groupby('Purchase Frequency')['Satisfaction Level'].mean())

# Özellik özetini çağır
check_features(data)


# Görselleştirme
plot_city_distribution(data)
plot_days_since_last_purchase(data)
plot_satisfaction_vs_discount(data)
plot_purchase_frequency_distribution(data)
plot_loyalty_score_kde(data)
plot_satisfaction_vs_loyalty(data)
plot_purchase_frequency_vs_satisfaction(data)
membership_spendingABTesting(data)
membership_satisfactionABTesting(data)

# High Spenders olup olmadıklarına ve indirim alıp almadıklarına göre Satisfaction Level ortalaması incelemesi
print(data['Satisfaction Level'])
print(data['Days Since Last Purchase'])
satisfaction_analysis = data.groupby(['Discount_and_High_Spend', 'High_Spender'])['Satisfaction Level'].mean().reset_index()
print(satisfaction_analysis)
