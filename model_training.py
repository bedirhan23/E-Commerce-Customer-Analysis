from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd


# Veriyi ve hedef değişkeni hazırlama fonksiyonu
def prepare_data(data, target_feature, additional_features=[]):
    features = ['Age', 'Total Spend', 'Items Purchased', 'Days Since Last Purchase'] + additional_features
    X = data[features]
    y = data[target_feature]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test


# Model eğitme fonksiyonu
def train_model(model, X_train, y_train):
    model.fit(X_train, y_train)
    return model


# Model değerlendirme fonksiyonu
def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    return mse, r2


# Tüm modeller için eğitim ve değerlendirme fonksiyonu
def train_and_evaluate_all_models(data, target_feature, additional_features=[]):
    # Only numeric features should be passed here
    additional_features = ['Satisfaction Level']  # Keep only the numeric ones
    X_train, X_test, y_train, y_test = prepare_data(data, target_feature, additional_features)

    models = {
        'Linear Regression': LinearRegression(),
        'Decision Tree': DecisionTreeRegressor(random_state=42),
        'Random Forest': RandomForestRegressor(random_state=42),
        'Gradient Boosting': GradientBoostingRegressor(random_state=42)
    }

    results = {}
    for model_name, model in models.items():
        model = train_model(model, X_train, y_train)
        mse, r2 = evaluate_model(model, X_test, y_test)
        results[model_name] = {'MSE': mse, 'R2 Score': r2}

    return results
