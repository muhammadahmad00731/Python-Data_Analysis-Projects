import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#data loading
df = pd.read_csv('project_3.csv')
#looking 5 rows
##print(df.head())
#___________________Data Cleaning
#checking duplicates
##print(df.duplicated(subset = ['Date','CustomerName','Product']))
#handling missing values
##print(df.isnull().sum())
#filling nulls (name, age)
df.fillna({"CustomerName":df['CustomerName'].mode()[0], "Age":df['Age'].mean()}, inplace = True)
#Checking for 'Total' column
##df["Total"] = df['Quantity'] * df["UnitPrice"]
#___________________Descriptive Analysis
#Total no. of orders
##print(f"Total No. of orders are: {df['Quantity'].sum()}")
#Unique Customers info
##print(f'Total unique customers are\n{df["CustomerName"].unique()}\nand their id is {df["OrderID"].unique()}')
#Total revenue
##print(f"Total Revenue is: {df['Total'].sum()}")
#Average Order value
##print(f"Average order value is: {df['UnitPrice'].mean()}")
#Average age
##print(f"Average age is: {df['Age'].mean().round(0)}")
##print(df.to_string())
#___________________Group & Aggregation
#Revenue by city
##print(df.groupby('City')['Total'].sum())
#Revenue by category
##print(df.groupby('Category')['Total'].sum())
#Top Selling Product
##print(df.groupby('Product')['Quantity'].sum().sort_values(ascending = False).head(1))
#Top Spending Customer
##print(df.groupby('CustomerName')['Total'].sum().sort_values(ascending = False).head(1))
#___________________Visualization_______________________________________________
### 1. Bar Chart → Sales by City
##city_sales = df.groupby("City")["Total"].sum()
##plt.figure(figsize=(6,4))
##city_sales.plot(kind="bar", color="skyblue", edgecolor="black")
##plt.title("Sales by City")
##plt.xlabel("City")
##plt.ylabel("Total Sales")
##plt.show()
##
### 2. Bar Chart → Sales by Category
##category_sales = df.groupby("Category")["Total"].sum()
##plt.figure(figsize=(6,4))
##category_sales.plot(kind="bar", color="orange", edgecolor="black")
##plt.title("Sales by Category")
##plt.xlabel("Category")
##plt.ylabel("Total Sales")
##plt.show()
##
### 3. Pie Chart → Gender Distribution
##gender_counts = df["Gender"].value_counts()
##plt.figure(figsize=(5,5))
##gender_counts.plot(kind="pie", autopct="%1.1f%%")
##plt.title("Customer Gender Distribution")
##plt.ylabel("")  # remove y-label
##plt.show()
##
# 4. Line Chart → Sales Trend by Date
##date_sales = df.groupby("Date")["Total"].sum()
##date_sales.plot(kind="line", marker="o", linestyle="-", color="green")
##plt.figure(figsize=(7,4))
##plt.title("Sales Trend Over Time")
##plt.xlabel("Date")
##plt.ylabel("Total Sales")
##plt.xticks(rotation=45)
##plt.show()