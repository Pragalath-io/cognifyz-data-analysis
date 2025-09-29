import pandas as pd

df = pd.read_csv('Dataset.csv')

city_with_most_restaurants = df['City'].value_counts().idxmax()
num_restaurants = df['City'].value_counts().max()

print(f"City with the highest number of restaurants: {city_with_most_restaurants} with {num_restaurants} restaurants.")

average_rating_per_city = df.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False)

print("\nAverage rating for restaurants in each city:")
print(average_rating_per_city)

city_with_highest_avg_rating = average_rating_per_city.idxmax()
highest_avg_rating = average_rating_per_city.max()

print(f"\nCity with the highest average rating: {city_with_highest_avg_rating} with an average rating of {highest_avg_rating:.2f}.")