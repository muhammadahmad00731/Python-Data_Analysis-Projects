import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Load CSV
df = pd.read_csv("synthetic_superstore_dataset_p2.csv")
#Handle missing values
##print(df.isnull().sum())
#Remove duplicates.
##print(df.duplicated().sum())
#Fixing Negative Values
##df["Profit"] = abs(df["Profit"])# we will redo it for a specific task at the end.
#Convert data types (Order Date, Ship Date → datetime).
order_dt = pd.to_datetime(df['OrderDate'])
ship_dt = pd.to_datetime(df['ShipDate'])
order_month = order_dt.dt.month
df["OrderMonth"] = order_month

#Create new columns: Total Sales = Quantity × Sales, Profit Margin = Profit / Sales
df["TotalSales"] = df["Quantity"] * df["Sales"]
df["ProfitMargin"] = df["Sales"] / df["Profit"]
#-------------------------------------------------------------------------------

##print(df.to_string())
#Summary stats:
##print(df.describe())
#Outlier detection (extremely high/low orders)
##q1 = np.percentile(df["Quantity"], 25)
##q2 = np.percentile(df["Quantity"], 50)
##q3 = (np.percentile(df["Quantity"], 75))
##IQR = q3 - q1
##left_outlier = q1 - (1.5 * IQR)
##right_outlier = q3 +  (1.5 * IQR)
##print(df[df["Quantity"] < left_outlier])
##print(df[df["Quantity"] > right_outlier])
#-------------------------------------------------------------------------------
#which products generate most sales & profit?
##print(df.groupby("Category")["TotalSales"].sum().sort_values(ascending = False).reset_index())
##print(df.groupby("SubCategory")["TotalSales"].sum().sort_values(ascending = False).reset_index())
#
##print(df.groupby("Category")["Profit"].sum().sort_values(ascending = False).reset_index())
##print(df.groupby("SubCategory")["Profit"].sum().sort_values(ascending = False).reset_index())
#By Region & State → which areas perform best?
##print(df.groupby("Region")["Quantity"].sum().sort_values(ascending = False).reset_index())
##print(df.groupby("State")["Quantity"].sum().sort_values(ascending = False).reset_index())
#By Ship Mode → is fast shipping more profitable?--->YES
##print(df.groupby("ShipMode")["Profit"].sum().sort_values(ascending = False).reset_index())
#Sales Analysis By Customer Segment (Consumer, Corporate, Home Office)
##print(df.groupby("Segment")["TotalSales"].sum().sort_values(ascending = False).reset_index())
#-------------------------------------------------------------------------------
#Sales trend over time (monthly sales line plot).
##x = df.groupby("OrderMonth")["TotalSales"].sum().reset_index()
##plt.figure(figsize = (9,5))
##plt.plot(x["OrderMonth"], x["TotalSales"], marker = 'o')
##plt.xticks(range(1,13))
##plt.xlabel("Months", color = "red")
##plt.ylabel("Sales", color = "red")
##plt.grid()
##plt.show()
#Which months/quarters are highest in sales?--->(Top 3 months)
##print(df.groupby("OrderMonth")["TotalSales"].sum().sort_values(ascending = False).reset_index().head(3))
#-------------------------------------------------------------------------------
##df["CustomerID"] = range(1, (len(df["OrderID"] ) +1))
#Top 10 customers by revenue.
##i = df.groupby("CustomerID")["TotalSales"].sum().reset_index()
##print(i)
#Segment customers into High Value / Medium / Low.
#High Value Customers
##print(df[i["TotalSales"]> 30000])
#-------------------------------------------------------------------------------
#Which products are sold at a loss (negative profit)?
##print(df[df["Profit"] < 0])
#Impact of discounts on profit (scatter plot of Discount vs Profit).
##plt.scatter(df["Discount"], df["Profit"], alpha=0.5)
##plt.xlabel("Discount")
##plt.ylabel("Profit")
##plt.title("Impact of Discount on Profit")
##plt.show()
#Which states/regions have high sales but low profit → opportunity for business strategy.
# Group by Region
##region_summary = df.groupby("Region")[["Sales", "Profit"]].sum().reset_index()
##print(region_summary)
# Group by State
##state_summary = df.groupby("State")[["Sales", "Profit"]].sum().reset_index()
##print(state_summary.sort_values("Profit").head(10))  # show lowest profit states