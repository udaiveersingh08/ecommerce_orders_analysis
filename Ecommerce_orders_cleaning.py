import pandas as pd 

udaiveersingh = pd.read_csv("01_ecommerce_orders.csv")

print(udaiveersingh.shape)
print(udaiveersingh.size)
print(udaiveersingh.describe(include="all"))



print(udaiveersingh.isna().sum())
print(udaiveersingh.duplicated().sum())


udaiveersingh["city"] = (
    udaiveersingh["city"].fillna("Unknown")
    .astype("string").str.strip().str.title()
)

udaiveersingh["payment_method"] = (
    udaiveersingh["payment_method"].fillna("Unknown")
    .astype("string").str.strip()
)

udaiveersingh["discount_pct"] = udaiveersingh["discount_pct"].fillna(0)
udaiveersingh["order_date"] = pd.to_datetime(udaiveersingh["order_date"], errors="coerce")
print(udaiveersingh)


udaiveersingh["gross_before_discount"] = udaiveersingh["quantity"] * udaiveersingh["unit_price"]
udaiveersingh["discount_amount"] = udaiveersingh["gross_before_discount"] * udaiveersingh["discount_pct"]
udaiveersingh["net_sales"] = udaiveersingh["gross_before_discount"] - udaiveersingh["discount_amount"]

udaiveersingh["order_month"] = udaiveersingh["order_date"].dt.to_period("M").astype("string")
print(udaiveersingh)


high_value = udaiveersingh.loc[
    udaiveersingh["net_sales"] >= 5000,
    ["order_id", "order_date", "city", "product", "net_sales"]
]
print("high_values_orders")
print(high_value)


Problem_orders = udaiveersingh.loc[
    udaiveersingh["order_status"].isin(["Returned", "Cancelled"])
]
print("problem_orders")
print(Problem_orders)


top_orders = udaiveersingh.sort_values("net_sales", ascending=False).head(10)
print(top_orders)

payment_counts = udaiveersingh["payment_method"].value_counts(dropna=False)
print(payment_counts)

mean_order = udaiveersingh["net_sales"].mean()
median_order = udaiveersingh["net_sales"].median()
print(mean_order , median_order)

monthly_counts = udaiveersingh["order_month"].value_counts().sort_index()
print(monthly_counts)

print(udaiveersingh["city"].value_counts())


udaiveersingh = udaiveersingh.to_csv("ecommerce_orders.cleaned.csv",index=False)
print(udaiveersingh)














