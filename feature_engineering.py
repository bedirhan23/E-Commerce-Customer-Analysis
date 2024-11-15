def add_recency_satisfaction(data):
    def recent_satisfaction(row):
        # Satisfaction Level ve Days Since Last Purchase'ın tipini kontrol et ve dönüştür
        try:
            satisfaction = int(row['Satisfaction Level'])
            days_since = int(row['Days Since Last Purchase'])
        except ValueError:
            raise ValueError("Satisfaction Level ve Days Since Last Purchase sayısal değerlere dönüştürülemiyor.")

        # Koşullara göre kategoriler atama
        if satisfaction >= 3 and days_since < 30:
            return "High Recency Satisfaction"
        elif satisfaction < 3 and days_since >= 30:
            return "Low Recency Satisfaction"
        else:
            return "Moderate Recency Satisfaction"

    data['Recent_Satisfaction'] = data.apply(recent_satisfaction, axis=1)
    return data


def add_satisfaction_dropoff(data):
    def satisfaction_dropoff(row):
        # Satisfaction Level ve Days Since Last Purchase'ın tipini kontrol et ve dönüştür
        try:
            satisfaction = int(row['Satisfaction Level'])
            days_since = int(row['Days Since Last Purchase'])
        except ValueError:
            raise ValueError("Satisfaction Level ve Days Since Last Purchase sayısal değerlere dönüştürülemiyor.")

        # Koşullara göre kategoriler atama
        if satisfaction <= 2 and days_since > 60:
            return "High Dropoff"
        elif satisfaction <= 2 and days_since <= 60:
            return "Moderate Dropoff"
        else:
            return "Low Dropoff"

    data['Satisfaction_Dropoff'] = data.apply(satisfaction_dropoff, axis=1)
    return data



def add_high_spender_discount_feature(data):
    # High Spender ve Discount ile ilgili özellikler
    data['High_Spender'] = data['Total Spend'] > data['Total Spend'].mean()
    data['Discount_and_High_Spend'] = data['High_Spender'] & data['Discount Applied']
    return data


def add_purchase_frequency(data):
    # Days Since Last Purchase'ı sınıflandır
    def purchase_frequency(row):
        try:
            days_since = int(row['Days Since Last Purchase'])
        except ValueError:
            raise ValueError("Days Since Last Purchase sayısal değere dönüştürülemiyor.")

        if days_since <= 30:
            return 'Frequent Buyer'
        elif days_since <= 90:
            return 'Occasional Buyer'
        else:
            return 'Rare Buyer'

    data['Purchase Frequency'] = data.apply(purchase_frequency, axis=1)
    return data


def add_loyalty_score(data):
    # Loyalty Score = Total Spend * Satisfaction Level
    try:
        data['Loyalty Score'] = data['Total Spend'] * data['Satisfaction Level'].astype(float)
    except ValueError:
        raise ValueError("Total Spend veya Satisfaction Level sayısal değere dönüştürülemiyor.")
    return data


def feature_engineering(data):
    data = add_recency_satisfaction(data)
    data = add_satisfaction_dropoff(data)
    data = add_high_spender_discount_feature(data)
    data = add_purchase_frequency(data)
    data = add_loyalty_score(data)
    return data
