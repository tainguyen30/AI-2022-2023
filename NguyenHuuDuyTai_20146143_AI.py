import pandas as pd
import numpy as np

# Read csv file from link
url = 'http://winterolympicsmedals.com/medals.csv'
df = pd.read_csv(url)

# Access "Medal" column to figure out which medal achieved the most & fewest and their quantities
medals_counts = df["Medal"].value_counts()
total_medals = str(sum(medals_counts))

# Access "Event Gender" column to figure out if American men or women participate in Olympic
gender_counts = df["Event gender"].value_counts()
total_athletics = str(sum(gender_counts))

# Access "City" column to figure out which city is selected to held Olympics games
city_counts = df["City"].value_counts()
most_selected_city = df["City"].value_counts().idxmax()
total_times = str(sum(city_counts))

# Access "Year" column to figure out which year gained the most medals
year_counts = df["Year"].value_counts()
most_gained_year = str(df["Year"].value_counts().idxmax())

# List the sports that gained medals from Olympics
sports = df["Sport"].unique()
total_nation = df["NOC"].value_counts()
nations = df["NOC"].unique()

# Release data
print(medals_counts)
print("The world has " + total_medals + " medals in Olympics\n")

print(gender_counts)
print("The world has " + total_athletics + " athletes participated in Olympics\n")

print(city_counts)
print(most_selected_city + " is the most selected city")
print("Olympic games were held " + total_times + " times\n")

print(year_counts)
print(most_gained_year + " is the most gained year")

print("Athletes participate in")
print(sports)
print("Total times each nation participating in Olympics: ")
print(total_nation)

