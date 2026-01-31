import streamlit as st

# ==================================
# Page Config
# ==================================
st.set_page_config(
    page_title="Retail Customer Segmentation & Analytics",
    layout="wide"
)

# ==================================
# Title
# ==================================
st.title(" Retail Customer Segmentation & Business Insights")

st.markdown(
    """
    This project uses **transaction data, RFM analysis, and machine learning–based clustering**
    to understand **customer behavior**, **revenue drivers**, and **growth opportunities**.

    The goal is to move beyond descriptive analytics and build a **data-driven customer segmentation**
    that directly supports **marketing, retention, and revenue decisions**.
    """
)

st.divider()

# ==================================
# What This Project Does
# ==================================
st.header(" Project Objective")

st.markdown(
    """
    This project:
    - Transforms raw retail transactions into **customer-level behavioral features**
    - Applies **RFM analysis** (Recency, Frequency, Monetary)
    - Uses **unsupervised machine learning (clustering)** to segment customers
    - Converts technical clusters into **business-friendly customer groups**
    - Connects insights to **clear, actionable recommendations**
    """
)

st.divider()

# ==================================
# Machine Learning & Segmentation
# ==================================
st.header(" Segmentation & Machine Learning Approach")

st.markdown(
    """
    Customer segmentation is built using **unsupervised learning**:

    - RFM features are engineered at the customer level
    - Features are scaled and prepared for clustering
    - Customers are grouped into **3 distinct clusters**
    - Clusters are interpreted and labeled as:
      **VIP**, **Solid Mid-Value**, and **Low-Value & Inactive**

    This approach allows the business to treat customers
    **differently based on real behavior, not assumptions**.
    """
)

st.divider()

# ==================================
# Dashboard Structure
# ==================================
st.header(" web app Overview")

st.markdown(
    """
    The  app follows a **logical decision-making flow**:
    """
)

st.subheader(" Tab 1 — Sales, Customer & Time Analysis")
st.markdown(
    """
    Explores revenue drivers across:
    customer behavior, product performance, geography,
    and time (month, weekday, hour).
    """
)


st.subheader(" Tab 2 — Final Insights & Executive Summary")
st.markdown(
    """
    Summarizes key findings and highlights
    the 80/20 revenue pattern for leadership.
    """
)


st.subheader(" Tab 3 — Customer Segmentation (RFM + ML)")
st.markdown(
    """
    Builds RFM features, applies clustering,
    and analyzes customer distribution and value by segment.
    """
)


st.subheader(" Tab 4 — Recommendations & Actions per Segment")
st.markdown(
    """
    Translates segmentation into
    concrete marketing, retention, and cost-control actions.
    """
)

st.divider()

# ==================================
# Final Summary
# ==================================
st.success(
    """
    **In Summary**
    
    This project demonstrates how **RFM analysis combined with machine learning**
    can turn raw transaction data into **clear customer segments**
    and **practical business strategies**.
    """
)
