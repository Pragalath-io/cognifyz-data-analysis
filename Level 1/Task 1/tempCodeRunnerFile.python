import pandas as pd

df = pd.read_csv('Dataset.csv')

online_delivery_counts = df['Has Online delivery'].value_counts()
restaurants_with_delivery = online_delivery_counts.get('Yes', 0)
total_restaurants = len(df)

percentage_with_delivery = (restaurants_with_delivery / total_restaurants) * 100

print(f"Percentage of restaurants that offer online delivery: {percentage_with_delivery:.2f}%")

average_ratings = df.groupby('Has Online delivery')['Aggregate rating'].mean()

print("\nAverage ratings:")
print(f"  - With online delivery: {average_ratings.get('Yes', 0):.2f}")
print(f"  - Without online delivery: {average_ratings.get('No', 0):.2f}")