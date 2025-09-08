import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import os

df=pd.read_csv("C:/Users/keert/OneDrive/Desktop/data_set/electronics.csv")

# Convert timestamp and extract month
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df['month'] = df['timestamp'].dt.month

numeric_df = df.select_dtypes(include='number')

output_folder = "EDA Outputs"
if not os.path.exists(output_folder):
    os.makedirs(output_folder) 

# ===== 1️⃣ Rating Distribution =====
plt.figure(figsize=(10,7))
sns.histplot(df['rating'], bins=5, kde=False)
plt.title("Rating Distribution")
full_path=os.path.join("EDA Outputs", "rating_distribution.png")
plt.savefig(full_path)
print(f"💾rating_distribution saved at:{full_path}")

# ===== 2️⃣ Brand Distribution =====
plt.figure(figsize=(10,5))
sns.countplot(x='brand', data=df)
plt.title("Brand Counts")
full_path=os.path.join("EDA Outputs", "brand_distribution.png")
plt.savefig(full_path)
print(f"💾brand_distribution saved at:{full_path}")

# ===== 3️⃣ Category Distribution =====
plt.figure(figsize=(10,5))
sns.countplot(x='category', data=df)
plt.title("Category Counts")
full_path=os.path.join("EDA Outputs", "category_distribution.png")  
plt.savefig(full_path)
print(f"💾category_distribution saved at:{full_path}")

# ===== 4️⃣ Time Trends =====
plt.figure(figsize=(8,4))
sns.countplot(x='month', data=df)
plt.title("Entries per Month")
full_path=os.path.join("EDA Outputs", "monthly_trends.png")
plt.savefig(full_path)
print(f"💾monthly_trends saved at:{full_path}")

# ===== 5️⃣ Correlation Heatmap =====
plt.figure(figsize=(10,8))
numeric_df = df.select_dtypes(include='number')
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
full_path = os.path.join(output_folder, "correlation_heatmap.png")
plt.savefig(full_path)
print(f"💾 correlation_heatmap saved at: {full_path}")
plt.close()