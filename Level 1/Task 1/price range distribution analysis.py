import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset.csv')

price_range_counts = df['Price range'].value_counts().sort_index()

plt.figure(figsize=(8, 6))
price_range_counts.plot(kind='bar', color='skyblue')
plt.title('Distribution of Price Ranges Among Restaurants')
plt.xlabel('Price Range')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--')

plt.savefig('price_range_distribution.png')

print("Generated a bar chart named 'price_range_distribution.png' to show the distribution of price ranges.")

price_range_percentage = df['Price range'].value_counts(normalize=True).sort_index() * 100

print("\nPercentage of restaurants in each price range category:")
for price_range, percentage in price_range_percentage.items():
    print(f"Price Range {price_range}: {percentage:.2f}%")