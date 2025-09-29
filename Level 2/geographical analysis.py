import pandas as pd
import folium

df = pd.read_csv('Dataset.csv')

center_lat = df['Latitude'].mean()
center_lon = df['Longitude'].mean()

restaurant_map = folium.Map(location=[center_lat, center_lon], zoom_start=12)

for index, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"{row['Restaurant Name']}<br>Cuisine: {row['Cuisines']}<br>Rating: {row['Aggregate rating']}",
        tooltip=row['Restaurant Name']
    ).add_to(restaurant_map)

restaurant_map.save('restaurant_locations.html')

print("Generated an interactive map named 'restaurant_locations.html'. Open this file in a browser to see the restaurant locations.")