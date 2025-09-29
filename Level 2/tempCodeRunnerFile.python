import pandas as pd

df = pd.read_csv('Dataset.csv')

restaurant_counts = df['Restaurant Name'].value_counts()

chains = restaurant_counts[restaurant_counts > 1].index.tolist()

df_chains = df[df['Restaurant Name'].isin(chains)]

print(f"Found {len(chains)} restaurant chains in the dataset.")

chain_analysis = df_chains.groupby('Restaurant Name').agg(
    Average_Rating=('Aggregate rating', 'mean'),
    Total_Votes=('Votes', 'sum'),
    Number_of_Outlets=('Restaurant Name', 'count')
).round(2)

popular_chains = chain_analysis.sort_values(by='Number_of_Outlets', ascending=False)

print("\n--- Analysis of Top 15 Largest Restaurant Chains ---")
print(popular_chains.head(15))

top_rated_chains = chain_analysis.sort_values(by='Average_Rating', ascending=False)

print("\n--- Analysis of Top 15 Highest-Rated Restaurant Chains ---")
print(top_rated_chains.head(15))