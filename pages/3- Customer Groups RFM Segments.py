import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================
# Page Config
# ==================================
st.set_page_config(
    page_title="Customer Segmentation (RFM)",
    layout="wide"
)

st.title(" Customer Segmentation (RFM Groups)")

st.markdown(
    """
    This page summarizes **customer segmentation** based on RFM analysis.  
    It shows **group-level metrics, distribution, revenue contribution, and business priority**.
    """
)

# ==================================
# Load RFM Segments & Profile
# ==================================
@st.cache_data
def load_rfm_segments():
    rfm_model = pd.read_csv('/Users/mohammedmahmood/Desktop/Data projects/Projects/Data science/Unsupervised proj/Retail Customer Segmentation Using RFM Analysis and/data/RFM_segments.csv')
    groups_profile = pd.read_csv('/Users/mohammedmahmood/Desktop/Data projects/Projects/Data science/Unsupervised proj/Retail Customer Segmentation Using RFM Analysis and/data/Groups_profile.csv')
    return rfm_model, groups_profile

rfm_model, groups_profile = load_rfm_segments()




# ==================================
# RFM Customer-Level Segments
# ==================================
st.subheader(" RFM Customer-Level Segmentation Data")

st.markdown(
    """
    Each row below represents **one customer** with their RFM behavior and assigned segment.

    🔹 Based on RFM clustering, customers are grouped into **3 distinct segments**:
    - **VIP** – High value, frequent, recent buyers  
    - **Solid Mid-Value** – Moderate engagement and spend  
    - **Low-Value & Inactive** – Low spend and long inactivity  

    This table is the **foundation** for all segment-level insights shown below.
    """
)

# Display full RFM customer-level table
st.dataframe(
    rfm_model.head(100),
    use_container_width=True
)

st.markdown(
    """
    **Key Columns Explained**
    - `CustomerID` → Unique customer identifier  
    - `Number_of_Orders` → Purchase frequency  
    - `Total_Spend` → Customer lifetime value  
    - `Days_Since_Last_Purchase` → Recency indicator  
    - `cluster` → Model-generated cluster label  
    - `group_name` → Business-friendly segment name  
    """
)

st.divider()

# ==================================
# 1️⃣ Display Group-Level Profile Table 
# ==================================
st.subheader("1️⃣ RFM Group Summary Table")

st.dataframe(groups_profile.style.format({
    "number_of_Customers": "{:,.0f}",
    "total_orders": "{:,.0f}",
    "median_orders": "{:,.0f}",
    "total_spend": "${:,.2f}",
    "median_spend": "${:,.2f}",
    "avg_recency_days": "{:.0f} days",
    "customer_%": "{:.1f}%",
    "revenue_%": "{:.1f}%"
}))

st.markdown(
    """
    **Insights**
    - VIP customers (~27%) contribute ~78% of revenue — top priority to retain.
    - Solid Mid-Value (~28.6%) contributes ~12% of revenue — focus on reactivation & upsell.
    - Low-Value & Inactive (~44%) contributes <10% of revenue — low-cost maintenance or suppress.
    """
)

st.divider()

# ==================================
# 2️⃣ Customer Distribution Pie Chart
# ==================================
st.subheader("2️⃣ Customer Distribution by Segment")

fig1 = px.pie(
    groups_profile,
    names=groups_profile.index,  # assuming group_name is index, otherwise use 'group_name'
    values='customer_%',
    title="Customer Distribution (%) by Segment",
    hole=0.4
)
st.plotly_chart(fig1, use_container_width=True)

# ==================================
# 3️⃣ Revenue Contribution Pie Chart
# ==================================
st.subheader("3️⃣ Revenue Contribution by Segment")

fig2 = px.pie(
    groups_profile,
    names=groups_profile.index,
    values='revenue_%',
    title="Revenue Contribution (%) by Segment",
    hole=0.4
)
st.plotly_chart(fig2, use_container_width=True)

st.markdown(
    """
    **Business Takeaway**
    - A small VIP group drives the majority of revenue.
    - Marketing and engagement efforts should be prioritized for high-value segments.
    """
)

st.divider()

# ==================================
# 4️⃣ Distribution of Recency, Orders, Spend
# ==================================
st.subheader("4️⃣ Segment Behavior Overview")

# Recency
fig3 = px.box(
    rfm_model,
    x="group_name",
    y="Days_Since_Last_Purchase",
    title="Recency (Days Since Last Purchase) by Segment",
    labels={"Days_Since_Last_Purchase": "Recency (Days)", "group_name": "Segment"}
)
st.plotly_chart(fig3, use_container_width=True)

# Orders
fig4 = px.box(
    rfm_model,
    x="group_name",
    y="Number_of_Orders",
    title="Number of Orders by Segment",
    labels={"Number_of_Orders": "Orders", "group_name": "Segment"}
)
st.plotly_chart(fig4, use_container_width=True)

# Spend
fig5 = px.box(
    rfm_model,
    x="group_name",
    y="Total_Spend",
    title="Total Spend by Segment",
    labels={"Total_Spend": "Total Spend ($)", "group_name": "Segment"}
)
st.plotly_chart(fig5, use_container_width=True)

st.markdown(
    """
    **Insights**
    - VIP: Low recency, high orders, high spend → top priority.
    - Solid Mid-Value: Medium recency and orders → target for upsell.
    - Low-Value & Inactive: High recency, low orders → minimal engagement.
    """
)

st.divider()

# ==================================
# 5️⃣ Optional: Highlight Top VIP Customers
# ==================================
st.subheader("5️⃣ Highlight Top VIP Customers")

top_vip = rfm_model[rfm_model['group_name'] == 'VIP'].sort_values('Total_Spend', ascending=False).head(10)
st.table(top_vip[['CustomerID', 'Number_of_Orders', 'Total_Spend', 'Days_Since_Last_Purchase']])
