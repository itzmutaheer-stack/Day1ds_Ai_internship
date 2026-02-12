import pandas as pd
Data={"customerID":[101,102,103,104,],
      "Name":["Mustakima","Heer",None,"Mutaheer"],
      "Age":[18,22,33,None],
      "City":["Kolkata","Kalaburgi",None," Hyderabad"]}

df=pd.DataFrame(Data)
print(df)

print("First rows:\n",df.head())
print("\nDataset info:")
print(df.info())

#missing value

print("\nMissing values per column:")
print(df.isna().sum())

#fill ,issimg values (statistical approach)

df["Age"]=df["Age"].fillna(df["Age"].mean())
df["Name"]=df["Name"].fillna("Unknown")
df["City"]=df["City"].fillna(df["City"].mode()[0])

# check data types before correction

print("\nData types BEFORE conversion")
print(df.dtypes)

# Task 1

import pandas as pd
import numpy as np

data = {
    "student_id": [1, 1, 3, 4, 5, 6, 1],
    "name": ["asif", "dalal", None, np.nan, "asif", "pig", "asif"],
    "city": ["bangalore", "gulbarga", None, np.nan, "wadi", "shabad", "bangalore"]
}

df = pd.DataFrame(data)

print("Shape BEFORE cleaning:", df.shape)

print("\nMissing Values Report:")
print(df.isna().sum())

numeric_columns = df.select_dtypes(include=['number']).columns

for col in numeric_columns:
    median_value = df[col].median()
    df[col] = df[col].fillna(median_value)

duplicate_count = df.duplicated().sum()
print("\nNumber of duplicate rows found:", duplicate_count)

df = df.drop_duplicates()

print("\nShape AFTER cleaning:", df.shape)

print("\nData cleaning completed successfully!")

#Task 2



import pandas as pd

df = pd.read_csv("customer_orders_clean.csv")

print("Data types before cleaning:")
print(df.dtypes)

df["Price"] = df["Price"].str.replace("$", "", regex=False)

df["Price"] = df["Price"].astype(float)

df["Date"] = pd.to_datetime(df["Date"])

print("\nData types after cleaning:")
print(df.dtypes)

#task 3
import pandas as pd

# Step 1: Load dataset
df = pd.read_csv("customer_orders_location.csv")

# Step 2: Check unique values before cleaning
print("Before Cleaning:")
print(df["Location"].unique())

# Step 3: Remove extra spaces
df["Location"] = df["Location"].str.strip()

# Step 4: Standardize text case (choose one)
df["Location"] = df["Location"].str.title()
# OR you can use:
# df["Location"] = df["Location"].str.lower()

# Step 5: Check unique values after cleaning
print("\nAfter Cleaning:")
print(df["Location"].unique())
      


             
      