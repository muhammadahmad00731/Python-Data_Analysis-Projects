import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("synthetic_retail_dataset.csv")
#Checking size
##print(df.shape)
#Checking datatypes
##print(df.dtypes)
#Checking NULLs
##print(df.isnull().sum())
#Checking Duplicates
##print(df.duplicated())
##print(df.duplicated().sum())
##print(df.duplicated().mean())
#_____________________________________________________________________________
# Handling Missing Values
CustomerID_mean = float(int(df['CustomerID'].mean()))
df = df.fillna({"Product":df['Product'].mode()[0] , "CustomerID": CustomerID_mean})

#Fix incorrect values (negative/zero Quantity)
df["Quantity"] = df["Quantity"].abs()
#_____________________________________________________________________________1972
#Create Column --> TotalPrice = Quantity × UnitPrice
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

#Extract Year, Month, Weekday, Hour from InvoiceDate
dt = pd.to_datetime(df['InvoiceDate'])
year = dt.dt.year
month = dt.dt.month
day = dt.dt.day
day_name = dt.dt.day_name()
hour = dt.dt.hour

df['Year'] = year
df['Month'] = month
df['Day'] = day
df['Day_Name'] = day_name
df['Hour'] = hour
##print(df.to_string())
#_____________________________________________________________________________
#Top Products → Top 10 by revenue & quantity
##print(df.groupby("Product")["TotalPrice"].sum().sort_values(ascending = False))

#Country Analysis → Revenue by country
##print(df.groupby("Country")["TotalPrice"].sum().sort_values(ascending = False))

#Customer Analysis → Top customers, purchase distribution
##print(df.groupby("CustomerID")["TotalPrice"].sum().sort_values(ascending = False))

#Sales Trends → Monthly revenue
##print(df.groupby("Month")["TotalPrice"].sum().sort_values(ascending = False))
#_____________________________________________________________________________
#Find unusually large orders
##q1 = np.percentile(df["TotalPrice"], 25)
##q2 = np.percentile(df["TotalPrice"], 50)
##q3 = (np.percentile(df["TotalPrice"], 75)).round(2)
##IQR = q3 - q1
##left_outlier = q1 - (1.5 * IQR)
##right_outlier = q3 +  (1.5 * IQR)
##print(df[df["TotalPrice"] > right_outlier])
#Visualize using boxplots
##df['TotalPrice'].plot(kind = 'box')
##plt.show()
#_____________________________________________________________________________
##Insights & Recommendations
#Which products drive most sales?
##print(df.groupby("Product")["Quantity"].sum().sort_values(ascending = False).head(1))
#Which country is most profitable?
##print(df.groupby("Country")["TotalPrice"].sum().sort_values(ascending = False).head(1))
#Who are the best customers?
##print(df.groupby("CustomerID")["TotalPrice"].sum().sort_values(ascending = False).head())
#Are there seasonal trends?
##monthly_sales = df.groupby('Month')['TotalPrice'].sum().reset_index()
##plt.plot(monthly_sales['Month'], monthly_sales['TotalPrice'], marker='o')
##plt.xticks(range(1,13))
##plt.xlabel("Month")
##plt.ylabel("Total Sales")
##plt.title("Monthly Sales Trend")
##plt.show()
