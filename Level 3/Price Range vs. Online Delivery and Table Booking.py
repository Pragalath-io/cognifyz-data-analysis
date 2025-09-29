import pandas as pd

df = pd.read_csv('Dataset.csv')

df['Has Online delivery'] = df['Has Online delivery'].apply(lambda x: 1 if x == 'Yes' else 0)
df['Has Table booking'] = df['Has Table booking'].apply(lambda x: 1 if x == 'Yes' else 0)

price_range_analysis = df.groupby('Price range')[['Has Online delivery', 'Has Table booking']].mean() * 100

price_range_analysis = price_range_analysis.rename(columns={
    'Has Online delivery': '% with Online Delivery',
    'Has Table booking': '% with Table Booking'
}).round(2)

print("--- Relationship Between Price Range and Services ---")
print(price_range_analysis)