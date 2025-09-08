import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder


# Load the dataset
print("=" * 100)
print("\n loading the dataset....\n")
print('=' * 100)
df=pd.read_csv("C:/Users/keert/OneDrive/Desktop/Amazon_electronics/electronics.csv")
print("First 10 rows of the dataset:")
print(df.head(10))

print("\ndataset information:")
print(df.info())

print("\nsummary statistics of the dataset:")
print(df.describe(include='all'))

print("="*100)
print("\nHandling missing values....\n")
print("="*100)

#check missing values
print("\nmissing value")
print(df.isnull().sum())

#fillna values
df['brand'].fillna('most_common_brand', inplace=True)

#dropna
df.dropna(subset=['user_attr'], inplace=True)

print("\nMissing values after handling:")
print(df.isnull().sum())

#timestamp converting datatype to datetime
df['timestamp']=pd.to_datetime(df['timestamp'], errors='coerce')

print("=" * 100)
print("\nEncoding Categorical Variables....\n")
print("=" * 100)

Categorical_columns=['brand', 'category',  'user_attr']
le = LabelEncoder()
for col in Categorical_columns:
    df[col]=le.fit_transform(df[col])
    print(f"Enoded {col}")
    print(df[col].head())

print("=" * 100)
print("\n verfying data types and cleanliness....\n")
print("=" * 100)
print("\nData types after encoding:")
print(df.dtypes)

#save the dataset to cleaned file
df.to_csv("C:/Users/keert/OneDrive/Desktop/Amazon_electronics/electronics_cleaned.csv", index=False)
print("\nCleaned dataset saved to 'electronics_cleaned.csv'")