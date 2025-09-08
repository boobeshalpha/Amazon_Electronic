# 📊 Amazon Electronics Data Analysis  

## 📌 Overview  
This project analyzes **Amazon Electronics dataset** to understand customer ratings, product categories, and brand trends. It includes:  
- **Data Cleaning & Preprocessing** (`electronics.py`)  
- **Exploratory Data Analysis (EDA)** with visualizations (`eda.py`)  

The workflow ensures raw data is cleaned, encoded, and then analyzed through descriptive statistics and plots.  

---

## 📂 Project Structure  
📁 Amazon_Electronics_Project
│── electronics.py # Data cleaning & preprocessing
│── eda.py # Exploratory Data Analysis & visualizations
│── electronics.csv # Raw dataset (not included in repo)
│── electronics_cleaned.csv # Cleaned dataset (generated)
│── EDA Outputs/ # Saved plots from EDA

yaml
Copy code

---

## ⚙️ Workflow  

### 🔹 1. Data Cleaning (`electronics.py`)  
- Loads raw dataset (`electronics.csv`)  
- Handles **missing values**:  
  - Fills missing `brand` with `"most_common_brand"`  
  - Drops rows with missing `user_attr`  
- Converts `timestamp` → datetime format  
- Encodes categorical columns (`brand`, `category`, `user_attr`) using **LabelEncoder**  
- Saves the cleaned dataset → `electronics_cleaned.csv`  

### 🔹 2. Exploratory Data Analysis (`eda.py`)  
- Loads cleaned dataset  
- Extracts **month** from `timestamp`  
- Generates plots:  
  - Rating distribution (`rating_distribution.png`)  
  - Brand counts (`brand_distribution.png`)  
  - Category counts (`category_distribution.png`)  
  - Monthly review trends (`monthly_trends.png`)  
  - Correlation heatmap (`correlation_heatmap.png`)  

All plots are saved in **`EDA Outputs/`** folder.  

---

## 📊 EDA Visualizations  

### ⭐ Rating Distribution  
![Rating Distribution](EDA%20Outputs/rating_distribution.png)  

### 🏷️ Brand Counts  
![Brand Distribution](EDA%20Outputs/brand_distribution.png)  

### 📦 Category Counts  
![Category Distribution](EDA%20Outputs/category_distribution.png)  

### 📈 Monthly Review Trends  
![Monthly Trends](EDA%20Outputs/monthly_trends.png)  

### 🔗 Correlation Heatmap  
![Correlation Heatmap](EDA%20Outputs/correlation_heatmap.png)  

---

## ▶️ How to Run  

1️⃣ **Run data cleaning**  
```bash
python electronics.py
Output → electronics_cleaned.csv

2️⃣ Run EDA

bash
Copy code
python eda.py
Output → Plots stored in EDA Outputs/

📦 Requirements
Install dependencies with:

bash
Copy code
pip install pandas matplotlib seaborn scikit-learn
📊 Example Insights
⭐ Ratings distribution helps identify customer satisfaction levels.

🏷️ Brand and category counts reveal top contributors in dataset.

📈 Monthly trends highlight seasonal patterns.

🔗 Correlation matrix shows relationships between numeric features.

🚀 Future Enhancements
Add sentiment analysis on review text.

Build a recommendation system using user-product interactions.

Deploy EDA results with Streamlit dashboard.

