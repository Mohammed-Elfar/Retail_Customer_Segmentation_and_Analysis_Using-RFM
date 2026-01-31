import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================
# Page Config
# ==================================
st.set_page_config(
    page_title="Sales, Customer & Time Analysis",
    layout="wide"
)

st.title(" Sales, Customer & Time Analysis")
st.markdown(
    """
    This dashboard explores **customer purchasing behavior** using transactional
    and RFM-based metrics to understand **what drives revenue**.
    """
)

# ==================================
# Load Data (ONE PLACE)
# ==================================

@st.cache_data
def load_rfm_analysis():
    return pd.read_csv('data/RFM_Analysis.csv')

@st.cache_data
def load_clean_transactions():
    return pd.read_csv('data/clean_transactions.csv')

rfm_df = load_rfm_analysis()
clean_df = load_clean_transactions()

# ==================================
# 1. Orders vs Total Spend
# ==================================
st.subheader("1️⃣ Do customers who place more orders spend more overall?")

fig1 = px.scatter(
    rfm_df,
    x="Number_of_Orders",
    y="Total_Spend",
    title="Number of Orders vs Total Spend",
    labels={
        "Number_of_Orders": "Number of Orders",
        "Total_Spend": "Total Spend"
    }
)

st.plotly_chart(fig1, use_container_width=True)

st.markdown(
    """
    **Insights**
    - Strong positive relationship between order frequency and total spend.
    - Most customers place few orders and contribute limited revenue.
    - A small group of frequent buyers generates most revenue.
    """
)

st.divider()

# ==================================
# 2. Product Diversity vs Total Spend
# ==================================
st.subheader("2️⃣ Do customers who buy more product types spend more?")

fig2 = px.scatter(
    rfm_df,
    x="Product_Diversity",
    y="Total_Spend",
    title="Product Diversity vs Total Spend",
    labels={
        "Product_Diversity": "Product Diversity",
        "Total_Spend": "Total Spend"
    }
)

st.plotly_chart(fig2, use_container_width=True)

st.markdown(
    """
    **Insights**
    - Customers buying a wider range of products tend to spend more.
    - High spenders usually have high product diversity.
    """
)

st.divider()

# ==================================
# 3. Customer Lifetime vs Total Spend
# ==================================
st.subheader("3️⃣ Do long-term customers always generate more revenue?")

fig3 = px.scatter(
    rfm_df,
    x="Customer_Lifetime_Days",
    y="Total_Spend",
    title="Customer Lifetime vs Total Spend",
    labels={
        "Customer_Lifetime_Days": "Customer Lifetime (Days)",
        "Total_Spend": "Total Spend"
    }
)

st.plotly_chart(fig3, use_container_width=True)

st.markdown(
    """
    **Insights**
    - Long customer lifetimes enable high revenue.
    - However, not all long-term customers are valuable.
    """
)

st.divider()

# ==================================
# 4. Bulk Buying vs Average Order Value
# ==================================
st.subheader("4️⃣ Do bulk buyers spend more or just buy cheaper items?")

fig4 = px.scatter(
    rfm_df,
    x="Total_Items_Purchased",
    y="Average_Order_Value",
    title="Bulk Buying vs Average Order Value",
    labels={
        "Total_Items_Purchased": "Total Items Purchased",
        "Average_Order_Value": "Average Order Value"
    }
)

st.plotly_chart(fig4, use_container_width=True)

st.markdown(
    """
    **Insights**
    - Customers who buy in bulk (high Total Items Purchased) do not necessarily spend more per order — in fact, the opposite is more common
    - bulk buyers are typically volume-driven (lots of low-price items), not value-driven (fewer expensive items)
    - Bulk buyers usually buy lots of cheap items rather than expensive ones — high average order value comes from customers who buy fewer, higher-priced products.”**
    
    """
)

st.divider()

# ==================================
# 5. Top Revenue Products
# ==================================
st.subheader("5️⃣ Which products drive the most revenue?")

top_products = (
    clean_df
    .groupby(["StockCode", "Description"], as_index=False)["Total_Price"]
    .sum()
    .sort_values("Total_Price", ascending=False)
    .head(20)
)

fig5 = px.bar(
    top_products,
    x="Total_Price",
    y="Description",
    orientation="h",
    title="Top 20 Revenue-Generating Products"
)

st.plotly_chart(fig5, use_container_width=True)

st.markdown(
    """
    **Insights**
    - The absolute #1 product by far is REGENCY CAKESTAND 3 TIER → generates over 120k in total revenue (clearly the standout winner)
    - Revenue is driven by a small number of hero products.
    - These products should be prioritized for inventory and promotions.
    - This highlights the importance of stock management and supply chain optimization for key products.
    """
)
st.divider()

# ==================================
# 6. Revenue by Country
# ==================================
st.subheader("6️⃣ Which countries generate the most revenue?")

country_revenue = (
    clean_df
    .groupby("Country", as_index=False)["Total_Price"]
    .sum()
    .sort_values("Total_Price", ascending=False)
)

fig6 = px.bar(
    country_revenue,
    x="Country",
    y="Total_Price",
    title="Revenue by Country",
    text_auto=True
)

st.plotly_chart(fig6, use_container_width=True)

st.markdown(
    """
    **Insights**
    - Revenue is highly concentrated in a few countries.
    - The UK dominates overall revenue.
    """
)

st.divider()

# ==================================
# 7. Monthly Revenue Trend
# ==================================
st.subheader("7️⃣ Which months are the strongest for sales?")

monthly_revenue = (
    clean_df
    .groupby("invoice_month", as_index=False)["Total_Price"]
    .sum()
)

fig7 = px.line(
    monthly_revenue,
    x="invoice_month",
    y="Total_Price",
    title="Monthly Revenue Trend"
)

st.plotly_chart(fig7, use_container_width=True)

st.markdown(
    """
    **Insights**
    - The absolute strongest month is month 10 (October) → highest revenue at around 1M+ (peak of the year)
    - Clear seasonality in revenue.
    - Strong peaks appear before Q4.
    """
)

st.divider()

# ==================================
# 8. Revenue by Weekday
# ==================================
st.subheader("8️⃣ Which days generate the highest revenue?")

weekday_revenue = (
    clean_df
    .groupby("invoice_weekday", as_index=False)["Total_Price"]
    .sum()
)

fig8 = px.bar(
    weekday_revenue,
    x="invoice_weekday",
    y="Total_Price",
    title="Revenue by Weekday",
    text_auto=True
)

st.plotly_chart(fig8, use_container_width=True)

st.markdown(
    """
    **Insights**
    - Mid-week days outperform weekends.
    - Sunday consistently underperforms.
    """
)

st.divider()

# ==================================
# 9. Revenue by Hour
# ==================================
st.subheader("9️⃣ What hours generate the most revenue?")

hourly_revenue = (
    clean_df
    .groupby("invoice_hour", as_index=False)["Total_Price"]
    .sum()
)

fig9 = px.line(
    hourly_revenue,
    x="invoice_hour",
    y="Total_Price",
    title="Revenue by Hour of Day"
)

st.plotly_chart(fig9, use_container_width=True)

st.markdown(
    """
    **Insights**
    - Peak revenue occurs between 10:00 and 12:00.
    - Sales drop sharply after late afternoon.
    """
)
