import pandas as pd

# ===============================
# ONLINE SHOPPING SALES ANALYSIS
# ===============================

# Load CSV file
try:
    df = pd.read_csv("online_shopping_sales.csv")
except FileNotFoundError:
    print("CSV file not found!")
    exit()

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Create Revenue column
df["Revenue"] = df["Quantity"] * df["Price"]

print("=" * 60)
print("ONLINE SHOPPING SALES ANALYSIS")
print("=" * 60)

print(df)

# --------------------------------
# BASIC KPIs
# --------------------------------

print("\n----- BASIC KPIs -----")

print("Total Orders:", len(df))
print("Total Customers:", df["Customer"].nunique())
print("Total Products:", df["Product"].nunique())
print("Total Revenue: ₹{:,.2f}".format(df["Revenue"].sum()))
print("Average Order Value: ₹{:,.2f}".format(df["Revenue"].mean()))
print("Total Quantity Sold:", df["Quantity"].sum())

# --------------------------------
# PRODUCT-WISE REVENUE
# --------------------------------

print("\n----- PRODUCT REVENUE -----")

print(
    df.groupby("Product")["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

# --------------------------------
# CATEGORY-WISE REVENUE
# --------------------------------

print("\n----- CATEGORY REVENUE -----")

print(
    df.groupby("Category")["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

# --------------------------------
# CITY-WISE SALES
# --------------------------------

print("\n----- CITY SALES -----")

print(
    df.groupby("City")["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

# --------------------------------
# PAYMENT METHOD ANALYSIS
# --------------------------------

print("\n----- PAYMENT METHODS -----")

print(
    df.groupby("Payment")["Revenue"]
      .sum()
)

# --------------------------------
# CUSTOMER ANALYSIS
# --------------------------------

print("\n----- CUSTOMER SPENDING -----")

customer_sales = (
    df.groupby("Customer")["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

print(customer_sales)

print("\nTop Customer:")

print(customer_sales.idxmax())

# --------------------------------
# MONTHLY SALES
# --------------------------------

df["Month"] = df["Date"].dt.strftime("%B")

print("\n----- MONTHLY SALES -----")

print(
    df.groupby("Month")["Revenue"]
      .sum()
)

# --------------------------------
# DAILY SALES
# --------------------------------

print("\n----- DAILY SALES -----")

print(
    df.groupby("Date")["Revenue"]
      .sum()
)

# --------------------------------
# HIGHEST ORDER
# --------------------------------

print("\nHighest Order")

print(
    df.loc[df["Revenue"].idxmax()]
)

# --------------------------------
# LOWEST ORDER
# --------------------------------

print("\nLowest Order")

print(
    df.loc[df["Revenue"].idxmin()]
)

# --------------------------------
# TOP 5 ORDERS
# --------------------------------

print("\nTop 5 Orders")

print(
    df.sort_values(
        by="Revenue",
        ascending=False
    ).head(5)
)

# --------------------------------
# REPEAT CUSTOMERS
# --------------------------------

print("\nRepeat Customers")

repeat = (
    df["Customer"]
      .value_counts()
)

print(
    repeat[repeat > 1]
)

# --------------------------------
# SUMMARY
# --------------------------------

print("\nSummary Statistics")

print(df.describe())

# --------------------------------
# SAVE REPORT
# --------------------------------

df.to_csv(
    "online_sales_report.csv",
    index=False
)

print("\nReport Saved Successfully!")

print("File Name : online_sales_report.csv")