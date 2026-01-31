import streamlit as st

# ==================================
# Page Config
# ==================================
st.set_page_config(
    page_title="Final Insights & Recommendations",
    layout="wide"
)

st.title(" Final Insights & Business Recommendations")

st.markdown(
    """
    This page summarizes **key business insights** derived from customer behavior,
    RFM analysis, and sales patterns — and translates them into **clear, actionable recommendations**.
    """
)

st.divider()

# ==================================
# Executive Summary
# ==================================
st.header(" Executive Summary")

st.markdown(
    """
    Our customer base follows a very strong **80/20 pattern**:

    - A **small group of frequent, long-term, variety-seeking customers** generates the majority of revenue.
    - The **United Kingdom dominates total revenue** (≈60–70%), followed by a few European countries.
    - Strong **seasonal peaks** appear in **September–October** (Q4 holiday shopping).
    - **Mid-week (Thursday)** and **late morning to early afternoon (10:00–12:00)** drive the highest sales.
    - Revenue is powered by a small set of **hero products**, led by **Regency Cakestand 3 Tier**.
    """
)

st.divider()

# ==================================
# Key Insights
# ==================================
st.header(" Key Insights – Core Patterns")

st.markdown(
    """
    ### 1️⃣ Frequency Drives Revenue
    - More orders = dramatically higher total spend.
    - Repeat buyers (30+ orders) are the true high-value customers.

    ### 2️⃣ Product Variety = Higher Value
    - Customers buying many different product types spend significantly more.
    - Variety seekers outperform single-category buyers by a wide margin.

    ### 3️⃣ Long Lifetime Helps — But Is Not Automatic
    - Longer relationships increase the chance of high spend.
    - Many long-term customers still remain low-value without engagement.

    ### 4️⃣ Bulk Buyers vs High-Ticket Buyers
    - Bulk buyers focus on **large quantities of cheap items** → low AOV.
    - High AOV comes from customers buying **fewer, more expensive products**.

    ### 5️⃣ Geographic Concentration
    - The UK is responsible for most revenue.
    - After the top 5 European countries, contribution drops sharply.

    ### 6️⃣ Seasonal & Time Patterns
    - Strongest months: **October > September**
    - Strongest weekday: **Thursday**
    - Strongest hours: **10:00–12:00**

    ### 7️⃣ Hero Products
    - Revenue is driven by a very small number of top-selling items:
      Regency Cakestand 3 Tier, White Hanging Heart T-Light Holder,
      Jumbo Bags, Party Bunting, decorative lights.
    """
)

st.divider()

# ==================================
# Strategic Recommendations
# ==================================
st.header(" Strategic Business Recommendations")

st.markdown(
    """
    ### 1️⃣ Protect & Grow Repeat and High-Value Customers
    - Build **loyalty and repeat-purchase programs** for customers with 5–20+ orders.
    - Give special treatment to **high-frequency + high-variety** customers:
      VIP offers, early access, exclusive deals.
    - Create a **VIP / Whale segment** (top 1–5% spenders) with dedicated care.

    ### 2️⃣ Focus Marketing & Inventory on Peak Times
    - Increase promotions during **September–October**, **Thursday**, and **10:00–12:00**.
    - Plan inventory and staffing ahead of **Q4 demand spikes**.
    - Reduce spend on low-performance periods (Sunday, evenings, November).

    ### 3️⃣ Double Down on Hero Products & Categories
    - Always keep **top 10–15 products** in stock.
    - Create **bundles** and **cross-sell recommendations** around hero products.
    - Encourage product exploration using “Customers also bought” strategies.

    ### 4️⃣ Geographic Focus
    - **Protect and grow the UK market** — primary revenue engine.
    - Invest selectively in strong European markets
      (Netherlands, Ireland, Germany, France).
    - Treat non-European markets as experimental and low priority.

    ### 5️⃣ Product & Customer Strategy
    - Push **high-ticket items** to increase average order value.
    - Use **retargeting and reminders** to convert one-time buyers into repeat customers.
    - Analyze why many long-term customers remain low-value and incentivize exploration.
    """
)

st.divider()

# ==================================
# Leadership Takeaway
# ==================================
st.header(" One-Liner for Leadership")

st.success(
    """
    “Our biggest revenue comes from repeat UK customers who buy many different items
    during mid-week in Q4 — we should protect our hero customers, time promotions perfectly,
    and convert more buyers into frequent, high-value customers.”
    """
)
