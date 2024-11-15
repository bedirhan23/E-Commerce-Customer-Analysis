from data_preprocessing import load_and_clean_data, preprocess_data
from feature_engineering import feature_engineering
from visualization import (
    plot_city_distribution, plot_days_since_last_purchase,
    plot_satisfaction_vs_discount, plot_purchase_frequency_distribution,
    plot_loyalty_score_kde, plot_satisfaction_vs_loyalty,
    plot_purchase_frequency_vs_satisfaction
)
from a_b_Testing import membership_spendingABTesting, membership_satisfactionABTesting
from model_training import train_and_evaluate_all_models


# Veri Yükleme ve Temizleme Fonksiyonu
def load_and_process_data(file_path):
    try:
        # Veri yükleme
        data = load_and_clean_data(file_path)
        # Preprocessing
        data = preprocess_data(data)
        # Özellik mühendisliği
        data = feature_engineering(data)
        return data
    except Exception as e:
        print(f"Veri işleme sırasında hata oluştu: {e}")
        raise


# Özelliklerin Özetini Yazdırma Fonksiyonu
def check_features(data):
    print("Discount_and_High_Spend Özeti:")
    print(data.groupby('Discount_and_High_Spend')['Satisfaction Level'].mean())
    print("\nPurchase Frequency Özeti:")
    print(data.groupby('Purchase Frequency')['Satisfaction Level'].mean())


# Görselleştirme Fonksiyonu
def visualize_data(data):
    plot_city_distribution(data)
    plot_days_since_last_purchase(data)
    plot_satisfaction_vs_discount(data)
    plot_purchase_frequency_distribution(data)
    plot_loyalty_score_kde(data)
    plot_satisfaction_vs_loyalty(data)
    plot_purchase_frequency_vs_satisfaction(data)


# A/B Testi Fonksiyonu
def run_ab_testing(data):
    membership_spendingABTesting(data)
    membership_satisfactionABTesting(data)


# Model Eğitim ve Değerlendirme Fonksiyonu
def train_and_evaluate_models(data, target_feature, additional_features):
    results = train_and_evaluate_all_models(data, target_feature, additional_features)
    for model_name, metrics in results.items():
        print(f"{model_name}: MSE = {metrics['MSE']}, R2 Score = {metrics['R2 Score']}")


# Ana Fonksiyon
def main():
    file_path = 'data/E-commerce Customer Behavior - Sheet1.csv'
    data = load_and_process_data(file_path)

    # Özellik özetlerini kontrol et
    check_features(data)

    # Görselleştirme
    visualize_data(data)

    # A/B Testi
    run_ab_testing(data)

    # Model Eğitim ve Değerlendirme
    additional_features = []  # Remove non-numeric features from here
    train_and_evaluate_models(data, 'Satisfaction Level', additional_features)


# Programın Çalıştırılması
if __name__ == "__main__":
    main()
