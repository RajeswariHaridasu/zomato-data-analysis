# ---------------------------------------------
# EDA - ZOMATO DATASET
# ---------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df=pd.read_excel("C:/Users/rharidas/Downloads/zomato_cleaned.xlsx")

#Distribution of Ratings
plt.figure(figsize=(8,5))

sns.histplot(df['rate'], bins=20)

plt.title("Distribution of Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")

plt.show()


#Distribution of Average Cost
plt.figure(figsize=(8,5))

sns.histplot(df['approx_cost(for two people)'], bins=30)

plt.title("Distribution of Cost")
plt.xlabel("Cost for Two")
plt.ylabel("Count")

plt.show()


# 3. Distribution of Votes (ZOOMED)
df_votes = df[df['votes'] < 1000]

plt.figure(figsize=(8,5))

sns.histplot(df_votes['votes'], bins=30)

plt.title("Distribution of Votes (Votes < 1000)")
plt.xlabel("Votes")
plt.ylabel("Count")

plt.show()


# 4. Restaurants per Location
plt.figure(figsize=(10,6))

df['location'].value_counts().head(10).plot(kind='bar')

plt.title("Top 10 Locations by Restaurant Count")
plt.xlabel("Location")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.show()


# 5. Restaurants per Restaurant Type
plt.figure(figsize=(10,6))

df['rest_type'].value_counts().head(10).plot(kind='bar')

plt.title("Top 10 Restaurant Types")
plt.xlabel("Restaurant Type")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.show()

# 6. Restaurants per Cuisine
plt.figure(figsize=(10,6))

df['cuisines'].value_counts().head(10).plot(kind='bar')

plt.title("Top 10 Cuisines")
plt.xlabel("Cuisine")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.show()