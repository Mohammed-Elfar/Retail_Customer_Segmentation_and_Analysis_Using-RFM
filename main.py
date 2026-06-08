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
st.title("Retail Customer Segmentation & Business Insights")

st.markdown(
    """
    This project uses **transaction data, RFM analysis, and machine learning clustering**
    to understand customer behavior, revenue drivers, and growth opportunities.

    The goal is to build a **data-driven customer segmentation** that directly supports
    marketing, retention, and revenue decisions.
    """
)

st.divider()

# ==================================
# Project Objective
# ==================================
st.header("Project Objective")

col_left, col_right = st.columns(2)

with col_left:
    st.markdown(
        """
        This project:
        - Transforms raw retail transactions into **customer-level behavioral features**
        - Applies **RFM analysis** (Recency, Frequency, Monetary)
        - Uses **unsupervised machine learning (K-Means)** to segment customers
        - Converts technical clusters into **business-friendly customer groups**
        - Connects every segment to **clear, targeted recommendations**
        """
    )

with col_right:
    st.info(
        """
        **Why RFM?**

        RFM captures the three dimensions that best predict future customer value:

        - **Recency** — How recently did they buy? Lower = more engaged.
        - **Frequency** — How many times have they bought?
        - **Monetary** — How much have they spent in total?
        """
    )

st.divider()

# ==================================
# Machine Learning Approach
# ==================================
st.header("Machine Learning Approach")

st.markdown(
    "Segmentation is built with **K-Means clustering (K = 4)**, selected using the elbow method "
    "and confirmed by the business clarity of each resulting segment."
)

step1, step2, step3, step4 = st.columns(4)

with step1:
    with st.container(border=True):
        st.markdown("**Step 1 — Feature Engineering**")
        st.caption(
            "Compute Recency, Frequency, and Monetary value "
            "per customer from raw transactions."
        )

with step2:
    with st.container(border=True):
        st.markdown("**Step 2 — Feature Scaling**")
        st.caption(
            "Standardize RFM features so no single dimension "
            "dominates clustering distance."
        )

with step3:
    with st.container(border=True):
        st.markdown("**Step 3 — K-Means (K = 4)**")
        st.caption(
            "Group customers into 4 behaviorally distinct clusters."
        )

with step4:
    with st.container(border=True):
        st.markdown("**Step 4 — Business Labeling**")
        st.caption(
            "Interpret each cluster by its RFM profile "
            "and assign an actionable business name."
        )

st.divider()

# ==================================
# The 4 Customer Segments
# ==================================
st.header("The 4 Customer Segments")

st.markdown(
    "Each segment has a distinct RFM profile and requires a different strategy:"
)

col_a, col_b = st.columns(2)

with col_a:
    st.success(
        """
        **VIP Champions**

        Purchased very recently (median 10 days ago), very frequently (median 7 orders),
        and spend the most (median $2,708 per customer).
        Only 25.2% of customers — but they generate **73.3% of all revenue**.

        Strategy: Retain, reward, and protect at all costs.
        """
    )
    st.warning(
        """
        **New One-Time Buyers**

        Made their first purchase within the last month (median 29 days ago)
        but have not returned yet. One order, $328 median spend.
        21.6% of customers — 3.7% of revenue.

        Strategy: Convert into repeat buyers before intent fades.
        """
    )

with col_b:
    st.info(
        """
        **Promising Mid-Tier Regulars**

        Have bought 3 times on average, solid spend ($1,013 median),
        but have not purchased in 2-3 months (median 71 days) — beginning to drift.
        28.8% of customers — 19.7% of revenue.

        Strategy: Re-engage and upsell before they go cold.
        """
    )
    st.error(
        """
        **Dormant One-Time Buyers**

        Bought once, spent the least ($237 median), and have been completely
        inactive for roughly 8 months (median 234 days).
        24.4% of customers — 3.2% of revenue.

        Strategy: One low-cost win-back attempt, then suppress.
        """
    )

st.divider()

# ==================================
# Dashboard Structure
# ==================================
st.header("App Structure")

p1, p2, p3, p4 = st.columns(4)

with p1:
    with st.container(border=True):
        st.markdown("**Page 1**")
        st.markdown("**Sales and Time Analysis**")
        st.caption(
            "Revenue across products, geography, and time periods."
        )

with p2:
    with st.container(border=True):
        st.markdown("**Page 2**")
        st.markdown("**Executive Summary**")
        st.caption(
            "Key findings and the 80/20 revenue pattern for leadership."
        )

with p3:
    with st.container(border=True):
        st.markdown("**Page 3**")
        st.markdown("**Customer Segmentation**")
        st.caption(
            "4-cluster RFM profiles, distributions, and customer explorer."
        )

with p4:
    with st.container(border=True):
        st.markdown("**Page 4**")
        st.markdown("**Recommendations**")
        st.caption(
            "Targeted actions and KPIs per segment."
        )

st.divider()

st.success(
    """
    **In Summary** — This project turns raw transaction data into 4 precise customer segments,
    each with a clear behavioral identity and a targeted strategy —
    from protecting top spenders to converting first-time buyers before their interest fades.
    """
)
