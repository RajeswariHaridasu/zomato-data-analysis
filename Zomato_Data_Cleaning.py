# ---------------------------------------------
# DATA CLEANING LOG - ZOMATO DATASET
# ---------------------------------------------

# 1. Import Libraries
import pandas as pd
import numpy as np

# ---------------------------------------------
# 2. Load Excel Dataset
# ---------------------------------------------
df = pd.read_excel("C:/Users/rharidas/Downloads/zomato.xlsx")

print("Original Shape:", df.shape)

# ---------------------------------------------
# 3. Remove Unnecessary Columns (Unnamed)
# ---------------------------------------------
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

print("After removing unnamed columns:", df.shape)

# ---------------------------------------------
# 4. Check Missing Values
# ---------------------------------------------
missing = df.isnull().sum()
missing_percent = (missing / len(df)) * 100

print("\nMissing Values:\n", missing)
print("\nMissing Percentage:\n", missing_percent)

# ---------------------------------------------
# 5. Drop Column with Too Many Missing Values
# ---------------------------------------------
df = df.drop(columns=['dish_liked'])

# ---------------------------------------------
# 6. Handle Important Missing Values
# ---------------------------------------------
df = df.dropna(subset=['rate', 'location', 'approx_cost(for two people)'])

# ---------------------------------------------
# 7. Remove Duplicates (Only Exact Duplicates)
# ---------------------------------------------
print("\nDuplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()

print("After removing duplicates:", df.shape)

# ---------------------------------------------
# 8. Fix Inconsistent Formatting
# ---------------------------------------------

# Clean rating column
df['rate'] = df['rate'].astype(str)
df['rate'] = df['rate'].str.replace('/5', '')
df['rate'] = pd.to_numeric(df['rate'], errors='coerce')

# Clean cost column
df['approx_cost(for two people)'] = df['approx_cost(for two people)'].astype(str)
df['approx_cost(for two people)'] = df['approx_cost(for two people)'].str.replace(',', '')
df['approx_cost(for two people)'] = pd.to_numeric(df['approx_cost(for two people)'], errors='coerce')

# ---------------------------------------------
# 9. Standardize Text Columns
# ---------------------------------------------
text_cols = ['location', 'rest_type', 'cuisines']

for col in text_cols:
    df[col] = df[col].str.lower().str.strip()

# ---------------------------------------------
# 10. Handle Outliers (IQR Method)
# ---------------------------------------------
Q1 = df['approx_cost(for two people)'].quantile(0.25)
Q3 = df['approx_cost(for two people)'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[(df['approx_cost(for two people)'] >= lower) &
        (df['approx_cost(for two people)'] <= upper)]

# ---------------------------------------------
# 11. Fill Remaining Missing Values
# ---------------------------------------------

# Fill important column
df = df.dropna(subset=['rate'])

# Fill optional columns
df['phone'] = df['phone'].fillna("not available")
df['menu_item'] = df['menu_item'].fillna("not specified")
df['listed_in(type)'] = df['listed_in(type)'].fillna("others")
df['listed_in(city)'] = df['listed_in(city)'].fillna("others")

# Fill categorical
df['rest_type'] = df['rest_type'].fillna("unknown")
df['cuisines'] = df['cuisines'].fillna("unknown")

# ---------------------------------------------
# 12. Create Derived Column
# ---------------------------------------------
def cost_category(cost):
    if cost < 500:
        return "Low"
    elif cost < 1000:
        return "Medium"
    else:
        return "High"

df['cost_category'] = df['approx_cost(for two people)'].apply(cost_category)

# ---------------------------------------------
# 13. Final Validation
# ---------------------------------------------
print("\nFinal Shape:", df.shape)

print("\nFinal Missing Values:\n", df.isnull().sum())

# ---------------------------------------------
# 14. Save Cleaned Dataset
# ---------------------------------------------
df.to_excel("C:/Users/rharidas/Downloads/zomato_cleaned.xlsx", index=False)

print("\nCleaned dataset saved successfully!")