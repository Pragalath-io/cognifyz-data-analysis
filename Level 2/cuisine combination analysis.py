import pandas as pd

df = pd.read_csv('Dataset.csv')

common_cuisines = df['Cuisines'].value_counts().head(10)

print("Top 10 most common cuisine combinations:")
print(common_cuisines)

cuisine_ratings = df.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False).head(10)

print("\nTop 10 cuisine combinations with the highest average ratings:")
print(cuisine_ratings)