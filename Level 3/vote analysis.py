import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Dataset.csv')

highest_votes = df.loc[df['Votes'].idxmax()]
print("--- Restaurant with the Highest Number of Votes ---")
print(highest_votes[['Restaurant Name', 'City', 'Cuisines', 'Aggregate rating', 'Votes']])

lowest_votes = df.loc[df['Votes'].idxmin()]
print("\n--- Restaurant with the Lowest Number of Votes ---")
print(lowest_votes[['Restaurant Name', 'City', 'Cuisines', 'Aggregate rating', 'Votes']])

correlation = df['Votes'].corr(df['Aggregate rating'])
print(f"\nCorrelation between number of votes and rating: {correlation:.2f}")

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Votes', y='Aggregate rating', alpha=0.5)
plt.title('Relationship Between Votes and Aggregate Rating')
plt.xlabel('Number of Votes')
plt.ylabel('Aggregate Rating')
plt.xscale('log')
plt.grid(True)
plt.savefig('votes_vs_rating_correlation.png')

print("\nGenerated a scatter plot named 'votes_vs_rating_correlation.png' to visualize the correlation.")