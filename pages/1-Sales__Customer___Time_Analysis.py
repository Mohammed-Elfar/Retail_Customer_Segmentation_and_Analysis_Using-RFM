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

# ==================================
# Data Loading
# All heavy groupby aggregations are pre-computed inside this cached function.
# They run once on first load and are served from cache on every subsequent render.
# ==================================

@st.cache_data
def load_data():
    rfm_df   = pd.read_csv("/mnt/user-data/uploads/RFM_Analysis.csv")
    clean_df = pd.read_csv("/mnt/user-data/uploads/clean_transactions.csv")
    return rfm_df, clean_df


@st.cache_data
def compute_aggregations(_clean_df):
    """
    Pre-compute all chart-level aggregations in a single pass.
    Underscore prefix on the parameter tells Streamlit not to hash the dataframe.
    Returns a dict of ready-to-plot dataframes.
    """
    top_products = (
        _clean_df
        .groupby(["StockCode", "Description"], as_index=False)["Total_Price"]
        .sum()
        .sort_values("Total_Price", ascending=False)
        .head(20)
    )

    country_revenue = (
        _clean_df
        .groupby("Country", as_index=False)["Total_Price"]
        .sum()
        .sort_values("Total_Price", ascending=False)
    )

    monthly_revenue = (
        _clean_df
        .groupby("invoice_month", as_index=False)["Total_Price"]
        .sum()
    )

    weekday_revenue = (
        _clean_df
        .groupby("invoice_weekday", as_index=False)["Total_Price"]
        .sum()
    )

    hourly_revenue = (
        _clean_df
        .groupby("invoice_hour", as_index=False)["Total_Price"]
        .sum()
    )

    return {
        "top_products":    top_products,
        "country_revenue": country_revenue,
        "monthly_revenue": monthly_revenue,
        "weekday_revenue": weekday_revenue,
        "hourly_revenue":  hourly_revenue,
    }


rfm_df, clean_df = load_data()
agg = compute_aggregations(clean_df)

# ==================================
# Page Header
# ==================================
st.title("Sales, Customer & Time Analysis")

st.markdown(
    """
    This page explores **customer purchasing behavior** using transactional and RFM-based metrics
    to understand what drives revenue across customers, products, geography, and time.
    """
)

st.divider()

# ==================================
# Section 1 — Orders vs Total Spend
# ==================================
st.subheader("1. Do customers who place more orders spend more overall?")

fig1 = px.scatter(
    rfm_df,
    x="Number_of_Orders",
    y="Total_Spend",
    title="Number of Orders vs Total Spend",
    labels={
        "Number_of_Orders": "Number of Orders",
        "Total_Spend":       "Total Spend",
    },
)
st.plotly_chart(fig1, use_container_width=True)

with st.expander("Insights"):
    st.markdown(
        """
        - Strong positive relationship between order frequency and total spend.
        - Most customers place few orders and contribute limited revenue.
        - A small group of frequent buyers generates the majority of revenue.
        """
    )

st.divider()

# ==================================
# Section 2 — Product Diversity vs Total Spend
# ==================================
st.subheader("2. Do customers who buy more product types spend more?")

fig2 = px.scatter(
    rfm_df,
    x="Product_Diversity",
    y="Total_Spend",
    title="Product Diversity vs Total Spend",
    labels={
        "Product_Diversity": "Product Diversity",
        "Total_Spend":        "Total Spend",
    },
)
st.plotly_chart(fig2, use_container_width=True)

with st.expander("Insights"):
    st.markdown(
        """
        - Customers buying a wider range of products tend to spend more.
        - High spenders almost always show high product diversity.
        """
    )

st.divider()

# ==================================
# Section 3 — Customer Lifetime vs Total Spend
# ==================================
st.subheader("3. Do long-term customers always generate more revenue?")

fig3 = px.scatter(
    rfm_df,
    x="Customer_Lifetime_Days",
    y="Total_Spend",
    title="Customer Lifetime vs Total Spend",
    labels={
        "Customer_Lifetime_Days": "Customer Lifetime (Days)",
        "Total_Spend":             "Total Spend",
    },
)
st.plotly_chart(fig3, use_container_width=True)

with st.expander("Insights"):
    st.markdown(
        """
        - Longer customer lifetimes create the opportunity for high revenue.
        - However, not all long-term customers are high value — engagement matters.
        """
    )

st.divider()

# ==================================
# Section 4 — Bulk Buying vs Average Order Value
# ==================================
st.subheader("4. Do bulk buyers spend more or just buy cheaper items?")

fig4 = px.scatter(
    rfm_df,
    x="Total_Items_Purchased",
    y="Average_Order_Value",
    title="Bulk Buying vs Average Order Value",
    labels={
        "Total_Items_Purchased": "Total Items Purchased",
        "Average_Order_Value":    "Average Order Value",
    },
)
st.plotly_chart(fig4, use_container_width=True)

with st.expander("Insights"):
    st.markdown(
        """
        - Customers who buy in bulk do not necessarily spend more per order.
        - Bulk buyers are typically volume-driven (many low-price items), not value-driven.
        - High average order value comes from customers who buy fewer, higher-priced products.
        """
    )

st.divider()

# ==================================
# Section 5 — Top Revenue Products
# ==================================
st.subheader("5. Which products drive the most revenue?")

fig5 = px.bar(
    agg["top_products"],
    x="Total_Price",
    y="Description",
    orientation="h",
    title="Top 20 Revenue-Generating Products",
    labels={"Total_Price": "Total Revenue", "Description": "Product"},
)
fig5.update_layout(yaxis=dict(autorange="reversed"))
st.plotly_chart(fig5, use_container_width=True)

with st.expander("Insights"):
    st.markdown(
        """
        - The top product by revenue is REGENCY CAKESTAND 3 TIER, generating over $120k — a clear standout.
        - Revenue is driven by a small number of hero products.
        - These products should be prioritized for inventory management and promotions.
        """
    )

st.divider()

# ==================================
# Section 6 — Revenue by Country
# ==================================
st.subheader("6. Which countries generate the most revenue?")

fig6 = px.bar(
    agg["country_revenue"],
    x="Country",
    y="Total_Price",
    title="Revenue by Country",
    labels={"Total_Price": "Total Revenue"},
    text_auto=True,
)
st.plotly_chart(fig6, use_container_width=True)

with st.expander("Insights"):
    st.markdown(
        """
        - Revenue is highly concentrated in a small number of countries.
        - The United Kingdom dominates overall revenue.
        """
    )

st.divider()

# ==================================
# Section 7 — Monthly Revenue Trend
# ==================================
st.subheader("7. Which months are the strongest for sales?")

fig7 = px.line(
    agg["monthly_revenue"],
    x="invoice_month",
    y="Total_Price",
    title="Monthly Revenue Trend",
    labels={"invoice_month": "Month", "Total_Price": "Total Revenue"},
)
st.plotly_chart(fig7, use_container_width=True)

with st.expander("Insights"):
    st.markdown(
        """
        - The strongest month is October (Month 10), reaching over $1M — the peak of the year.
        - Clear seasonality with strong demand before Q4 holiday shopping.
        """
    )

st.divider()

# ==================================
# Section 8 — Revenue by Weekday
# ==================================
st.subheader("8. Which days generate the highest revenue?")

fig8 = px.bar(
    agg["weekday_revenue"],
    x="invoice_weekday",
    y="Total_Price",
    title="Revenue by Weekday",
    labels={"invoice_weekday": "Day of Week", "Total_Price": "Total Revenue"},
    text_auto=True,
)
st.plotly_chart(fig8, use_container_width=True)

with st.expander("Insights"):
    st.markdown(
        """
        - Mid-week days consistently outperform weekends.
        - Sunday is the lowest-performing day of the week.
        """
    )

st.divider()

# ==================================
# Section 9 — Revenue by Hour
# ==================================
st.subheader("9. What hours generate the most revenue?")

fig9 = px.line(
    agg["hourly_revenue"],
    x="invoice_hour",
    y="Total_Price",
    title="Revenue by Hour of Day",
    labels={"invoice_hour": "Hour of Day", "Total_Price": "Total Revenue"},
)
st.plotly_chart(fig9, use_container_width=True)

with st.expander("Insights"):
    st.markdown(
        """
        - Peak revenue occurs between 10:00 and 12:00.
        - Sales drop sharply after mid-afternoon and are minimal in the evening.
        """
    )
