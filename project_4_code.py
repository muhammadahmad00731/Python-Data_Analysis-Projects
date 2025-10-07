import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#------------loading data--------------
df = pd.read_csv("Retail_Sales.csv")
##print(df.to_string())
#------------basic information---------
##print(df.head(10))
##print(df.info()) # checking datatypes
##print(df.dtypes) # checking datatypes
##print(df.describe())
#------------checking nulls---------
##print(df.isnull().sum())
##print(df.isnull().mean())
#------------checking deplicates---------
##print(df.duplicates())
##print(df.duplicated().sum())
#------------changing datatype---------
dt = pd.to_datetime(df['Order_Date'])
#------------creating year column---------
df["year"] = dt.dt.year
##print(df.to_string())
#------------EDA---------
# Top 5 selling products
##print(df.groupby("Product_Name")["Quantity"].sum().sort_values(ascending=False).head(5).reset_index())
# top 5 profitable products
##print(df.groupby("Product_Name")["Profit"].sum().sort_values(ascending=False).head(5).reset_index())
# region with highest sales
##print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False).head(5).reset_index())
# category with highest profit
##print(df.groupby("Category")["Profit"].sum().sort_values(ascending=False).head(5).reset_index())
# Total Sales
##print(df["Sales"].sum())
# Total Profit
##print(df["Profit"].sum())
# Total Quantity
##print(df["Quantity"].sum())
#------------Data Visualization---------
# Sales by Category
##x = df.groupby("Category")["Sales"].sum().head(5).reset_index()
##plt.bar(x["Category"], x["Sales"])
##plt.show()
# Profit by Region
##x = df.groupby("Region")["Profit"].sum().head(5).reset_index()
##plt.bar(x["Region"], x["Profit"])
##plt.show()
#Sales Trend over Time
##df["Month"] = dt.dt.month
##x = df.groupby("Month")["Sales"].sum().reset_index()
##plt.plot(x["Month"], x["Sales"], marker = 'o')
##plt.xticks(range(1,13))
##plt.grid()
##plt.show()
# Share of each Category in Total Sales
##x = df.groupby("Category")["Sales"].sum().reset_index()
##plt.pie(x["Sales"], labels = x["Category"], explode = [0,0.2,0] , colors  = ["red","orange","blue"])
##plt.show()