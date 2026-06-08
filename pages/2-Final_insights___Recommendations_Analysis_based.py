import streamlit as st

# ==================================
# Page Config
# ==================================
st.set_page_config(
    page_title="Final Insights & Recommendations",
    layout="wide"
)

# ==================================
# Title
# ==================================
st.title("Final Insights & Business Recommendations")

st.markdown(
    """
    This page summarizes **key business insights** derived from customer behavior,
    RFM analysis, and sales patterns — and translates them into
    **clear, actionable recommendations**.
    """
)

st.divider()

# ==================================
# Executive Summary
# ==================================
st.header("Executive Summary")

st.markdown(
    """
    The customer base follows a strong **80/20 pattern**:

    - A **small group of frequent, long-term, variety-seeking customers** generates the majority of revenue.
    - The **United Kingdom dominates total revenue** (approximately 60-70%), followed by a few European countries.
    - Strong **seasonal peaks** appear in **September-October** (Q4 holiday shopping).
    - **Mid-week (Thursday)** and **late morning (10:00-12:00)** drive the highest daily sales.
    - Revenue is powered by a small set of **hero products**, led by **Regency Cakestand 3 Tier**.
    """
)

st.divider()

# ==================================
# Key Insights
# ==================================
st.header("Key Insights")

col_left, col_right = st.columns(2)

with col_left:
    with st.container(border=True):
        st.markdown("**1. Frequency Drives Revenue**")
        st.markdown(
            """
            More orders correlates directly with dramatically higher total spend.
            Repeat buyers with 30+ orders are the true high-value customers.
            """
        )

    with st.container(border=True):
        st.markdown("**2. Product Variety Signals Higher Value**")
        st.markdown(
            """
            Customers who buy across many product categories spend significantly more.
            Variety seekers outperform single-category buyers by a wide margin.
            """
        )

    with st.container(border=True):
        st.markdown("**3. Long Lifetime Helps — But Is Not Automatic**")
        st.markdown(
            """
            Longer relationships increase the chance of high spend,
            but many long-term customers remain low-value without active engagement.
            """
        )

    with st.container(border=True):
        st.markdown("**4. Bulk Buyers vs High-Ticket Buyers**")
        st.markdown(
            """
            Bulk buyers purchase large quantities of cheap items — low average order value.
            High average order value comes from customers buying fewer, more expensive products.
            """
        )

with col_right:
    with st.container(border=True):
        st.markdown("**5. Geographic Concentration**")
        st.markdown(
            """
            The UK accounts for the majority of revenue.
            After the top 5 European countries, contribution drops sharply.
            """
        )

    with st.container(border=True):
        st.markdown("**6. Seasonal and Time Patterns**")
        st.markdown(
            """
            - Strongest months: **October, then September**
            - Strongest weekday: **Thursday**
            - Strongest hours: **10:00-12:00**
            """
        )

    with st.container(border=True):
        st.markdown("**7. Hero Products**")
        st.markdown(
            """
            A very small number of products drive the bulk of revenue:
            Regency Cakestand 3 Tier, White Hanging Heart T-Light Holder,
            Jumbo Bags, Party Bunting, and decorative lights.
            """
        )

st.divider()

# ==================================
# Strategic Recommendations
# ==================================
st.header("Strategic Business Recommendations")

rec1, rec2 = st.columns(2)

with rec1:
    with st.container(border=True):
        st.markdown("**1. Protect and Grow Repeat and High-Value Customers**")
        st.markdown(
            """
            - Build **loyalty and repeat-purchase programs** for customers with 5-20+ orders.
            - Give dedicated treatment to **high-frequency, high-variety** customers:
              exclusive offers, early access, personalized deals.
            - Create a dedicated segment (top 1-5% spenders) with concierge-level care.
            """
        )

    with st.container(border=True):
        st.markdown("**2. Focus Marketing and Inventory on Peak Periods**")
        st.markdown(
            """
            - Increase promotions during **September-October**, **Thursday**, and **10:00-12:00**.
            - Plan inventory and staffing ahead of **Q4 demand spikes**.
            - Reduce spend on low-performance periods (Sunday, evenings, November onward).
            """
        )

    with st.container(border=True):
        st.markdown("**3. Double Down on Hero Products and Categories**")
        st.markdown(
            """
            - Always keep **top 10-15 products** in stock — zero stockouts on these items.
            - Create **bundles and cross-sell recommendations** around hero products.
            - Encourage product exploration with "Customers also bought" strategies.
            """
        )

with rec2:
    with st.container(border=True):
        st.markdown("**4. Geographic Focus**")
        st.markdown(
            """
            - **Protect and grow the UK market** — the primary revenue engine.
            - Invest selectively in strong European markets
              (Netherlands, Ireland, Germany, France).
            - Treat non-European markets as experimental and low priority.
            """
        )

    with st.container(border=True):
        st.markdown("**5. Product and Customer Conversion Strategy**")
        st.markdown(
            """
            - Push **high-ticket items** to increase average order value.
            - Use **post-purchase automation** to convert one-time buyers into repeat customers.
            - Analyze why long-term customers stay low-value and design incentives
              to increase their purchase frequency and category breadth.
            """
        )

st.divider()

# ==================================
# Leadership Takeaway
# ==================================
st.header("Leadership Takeaway")

st.success(
    """
    Our biggest revenue comes from repeat UK customers who buy many different items
    during mid-week in Q4. We should protect our highest-value customers, time promotions
    precisely, and systematically convert more buyers into frequent, high-value customers.
    """
)
