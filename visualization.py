# visualization.py

import matplotlib
matplotlib.use('TkAgg')  # Set backend before importing pyplot
import matplotlib.pyplot as plt
import seaborn as sns

def plot_city_distribution(data):
    plt.figure(figsize=(12, 12))
    sns.countplot(x='City', data=data, palette='viridis')
    plt.xlabel('City')
    plt.ylabel('Count')
    plt.title('City by Count')
    plt.xticks(rotation=45)
    plt.legend([], [], frameon=False)  # Legend'ı gizlemek için
    plt.show()

def plot_days_since_last_purchase(data):
    plt.figure(figsize=(8, 8))
    sns.histplot(data['Days Since Last Purchase'], color='green')
    plt.title("Distribution of Days Since Last Purchase")
    plt.show()

def plot_satisfaction_vs_discount(data):
    data['Discount_and_High_Spend'] = data['Discount_and_High_Spend'].astype(str)

    # Satisfaction Level ortalamalarını gruplama ve bar plot ile görselleştirme
    satisfaction_means = data.groupby('Discount_and_High_Spend')['Satisfaction Level'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Discount_and_High_Spend', y='Satisfaction Level', data=satisfaction_means, palette='viridis')
    plt.xlabel("High Spender with Discount")
    plt.ylabel("Average Satisfaction Level")
    plt.title("Average Satisfaction Level by Discount and High-Spending Status")
    plt.show()

def plot_purchase_frequency_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Purchase Frequency', data=data, palette='Set2')
    plt.xlabel("Purchase Frequency")
    plt.ylabel("Count")
    plt.title("Distribution of Purchase Frequency among Customers")
    plt.legend([], [], frameon=False)  # Legend'ı gizlemek için
    plt.show()

def plot_loyalty_score_kde(data):
    """
    Plots the Kernel Density Estimate (KDE) of the Loyalty Score.

    Parameters:
    - data: DataFrame containing a 'Loyalty Score' column.
    """
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data['Loyalty Score'], shade=True, color="purple")
    plt.xlabel("Loyalty Score")
    plt.ylabel("Density")
    plt.title("Kernel Density Estimate of Loyalty Score")
    plt.show()

def plot_satisfaction_vs_loyalty(data):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Satisfaction Level', y='Loyalty Score', hue='High_Spender', data=data, palette='coolwarm')
    plt.xlabel("Satisfaction Level")
    plt.ylabel("Loyalty Score")
    plt.title("Relationship between Satisfaction Level and Loyalty Score")
    plt.legend(title="High Spender", loc='upper left')
    plt.show()

def plot_purchase_frequency_vs_satisfaction(data):
    plt.figure(figsize=(10, 6))
    sns.violinplot(x='Purchase Frequency', y='Satisfaction Level', data=data, palette='Set3')
    plt.xlabel("Purchase Frequency")
    plt.ylabel("Satisfaction Level")
    plt.title("Satisfaction Level by Purchase Frequency")
    plt.show()
