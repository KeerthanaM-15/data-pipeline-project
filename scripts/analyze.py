# ============================================
# PROJECT: Superstore Sales Analysis
# ============================================

import pandas as pd

# LOAD THE DATA
df = pd.read_csv('D:\data-pipeline-project\data\superstore.csv', encoding='latin-1')

# STEP 1: PEEK AT THE DATA
print("=== First 5 rows of data ===")
print(df.head())

# STEP 2: SIZE OF DATA
print("\n=== Dataset Size ===")
print(f"Total Rows: {df.shape[0]}")
print(f"Total Columns: {df.shape[1]}")

# STEP 3: COLUMN NAMES
print("\n=== Column Names ===")
print(df.columns.tolist())

# STEP 4: TOTAL SALES
print("\n=== Total Revenue ===")
total = df['Sales'].sum()
print(f"Total Sales: ${total:,.2f}")

# STEP 5: SALES BY CATEGORY
print("\n=== Sales by Category ===")
print(df.groupby('Category')['Sales'].sum().sort_values(ascending=False))

# STEP 6: TOP 5 STATES BY SALES
print("\n=== Top 5 States by Sales ===")
print(df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(5))

# STEP 7: PROFIT BY CATEGORY
print("\n=== Profit by Category ===")
print(df.groupby('Category')['Profit'].sum().sort_values(ascending=False))