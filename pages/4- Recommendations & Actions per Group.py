import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================
# TAB 4 – Recommendations & Actions
# ==================================
st.title(" Recommendations & Actions per Customer Group")

st.markdown(
    """
    Based on RFM clustering, customers are segmented into **3 distinct groups**.
    Each group differs significantly in **value, behavior, and business priority**.

    The table below summarizes the **final customer segmentation** used for strategic decisions.
    """
)

st.divider()

# ==================================
# Final Segmentation Summary Table
# ==================================
st.subheader(" Final Customer Segmentation Summary")

segmentation_summary = pd.DataFrame({
    "Cluster": [1, 2, 0],
    "Segment Name": ["VIP", "Solid Mid-Value", "Low-Value & Inactive"],
    "% Customers": ["27.0%", "28.6%", "44.4%"],
    "% Revenue": ["78.3%", "12.1%", "9.5%"],
    "Avg Recency (days)": ["~27", "~44", "~165"],
    "Typical Orders": ["6+", "2", "1–2"],
    "Median Spend": ["~2,356", "~645", "~276"],
    "Business Meaning & Priority": [
        "Recent high-value repeat buyers – Highest priority – protect & grow",
        "Occasional / lapsed mid-value – Medium priority – reactivate & upsell",
        "Low spend, mostly inactive – Lowest priority – low-cost or suppress"
    ]
})

st.dataframe(segmentation_summary, use_container_width=True)

st.divider()

# ==================================
# Strategic Recommendations
# ==================================
st.header(" Strategic Recommendations by Segment")

# -------------------------------
# VIP Segment
# -------------------------------
st.subheader(" VIP Customers — Core Revenue Drivers")

st.markdown(
    """
    **Profile**
    - Represent only **27% of customers**
    - Generate **over 78% of total revenue**
    - Very recent, frequent, and high-spending

    **Actions**
    - ⭐ **Highest priority — protect at all costs**
    - Personalized offers and exclusive promotions
    - Early access to new products and seasonal collections
    - Loyalty rewards and VIP programs
    - Never allow stockouts on products they frequently purchase
    - Monitor churn signals **weekly** (increasing recency is a red flag)
    """
)

st.divider()

# -------------------------------
# Solid Mid-Value Segment
# -------------------------------
st.subheader(" Solid Mid-Value Customers — Main Growth Opportunity")

st.markdown(
    """
    **Profile**
    - ~29% of customers
    - Moderate revenue contribution (12%)
    - Less frequent and slightly lapsed behavior

    **Actions**
    - **Medium priority — focus on upgrading**
    - Cross-sell and upsell campaigns (bundles, recommendations)
    - Incentives for repeat purchases (free shipping thresholds, points)
    - Reactivation offers for customers with increasing recency
    - Encourage product variety to mimic VIP behavior
    """
)

st.divider()

# -------------------------------
# Low-Value & Inactive Segment
# -------------------------------
st.subheader(" Low-Value & Inactive Customers — Cost Control Segment")

st.markdown(
    """
    **Profile**
    - Largest group (~44% of customers)
    - Very low revenue contribution (<10%)
    - Long inactivity and low engagement

    **Actions**
    -  **Lowest priority — minimize marketing cost**
    - Only low-cost automated win-back campaigns
      (e.g. one “We miss you” email every 3–6 months)
    - Suppress from expensive channels (paid ads, SMS)
    - Focus acquisition budget on finding **new high-potential customers**
    """
)

st.divider()

# ==================================
# Executive Takeaway
# ==================================
st.success(
    """
    **Leadership Takeaway**
    
    Revenue is driven by a small VIP segment.
    Business impact comes from protecting high-value customers
    and systematically converting mid-value customers into VIPs,
    while tightly controlling costs on low-value segments.
    """
)
