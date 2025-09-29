import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Dataset.csv')

plt.figure(figsize=(10, 6))
sns.histplot(df['Aggregate rating'], bins=20, kde=True, color='teal')
plt.title('Distribution of Aggregate Restaurant Ratings')
plt.xlabel('Aggregate Rating')
plt.ylabel('Number of Restaurants')
plt.grid(axis='y', linestyle='--')
plt.savefig('rating_distribution.png')

print("Generated a histogram named 'rating_distribution.png' to show the distribution of aggregate ratings.")

most_common_rating = df['Aggregate rating'].astype(int).mode()[0]
print(f"\nThe most common integer rating for restaurants is: {most_common_rating}")

average_votes = df['Votes'].mean()

print(f"\nThe average number of votes received by restaurants is: {average_votes:.2f}")