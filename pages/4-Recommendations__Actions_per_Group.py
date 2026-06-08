import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================
# Page Config
# ==================================
st.set_page_config(
    page_title="Recommendations & Actions",
    layout="wide"
)

# ==================================
# Segment Configuration
# Must stay in sync with Page 3 SEGMENT_CONFIG.
# Raw CSV group_name values map to correct business labels based on actual RFM behavior.
# ==================================

SEGMENTS = [
    {
        "raw_name":      "Early Lifecycle",   # CSV group_name (label is misleading)
        "display":       "VIP Champions",
        "priority":      1,
        "action":        "Retain",
        "color":         "#EF9F27",
        "customers_pct": "25.2%",
        "revenue_pct":   "73.3%",
        "median_recency":"10 days",
        "median_orders": "7",
        "median_spend":  "$2,708",
        "who_they_are": (
            "Your best customers across every RFM dimension simultaneously. "
            "They bought very recently (median 10 days ago), very often (median 7 orders), "
            "and spend the most per customer (median $2,708). "
            "They represent only 25% of the customer base but generate 73.3% of all revenue. "
            "Losing even a small fraction of this group has an outsized revenue impact."
        ),
        "actions": [
            "Protect first — monitor recency weekly and flag anyone approaching 30 days since last purchase as at-risk.",
            "Run a dedicated VIP loyalty program with exclusive tiers, early product access, and personalized offers.",
            "Provide personalized product recommendations based on individual purchase history, not generic promotions.",
            "Ensure zero stockouts on the product categories this group buys most.",
            "Assign account managers or concierge service to the top 5% of spenders within this group.",
            "Track each customer's purchase cadence — if a normal 2-week cycle stretches to 4 weeks, trigger a personal outreach.",
        ],
        "kpi":    "Champion churn rate (monthly). A 5% improvement recovers approximately 3.5% of total revenue.",
        "budget": "High — this group justifies premium investment across all channels.",
    },
    {
        "raw_name":      "Mid_Value",
        "display":       "Promising Mid-Tier Regulars",
        "priority":      2,
        "action":        "Grow",
        "color":         "#3266ad",
        "customers_pct": "28.8%",
        "revenue_pct":   "19.7%",
        "median_recency":"71 days",
        "median_orders": "3",
        "median_spend":  "$1,013",
        "who_they_are": (
            "Customers who have shown genuine loyalty — bought 3 times on average "
            "and spend over $1,000 — but have not purchased in 2-3 months (median 71 days). "
            "They are the largest segment by count (28.8%) and the clearest growth opportunity: "
            "they already trust the brand and just need a reason to return more often. "
            "Left unattended, they will drift toward the Dormant segment."
        ),
        "actions": [
            "Re-engage at the 60-day mark — automated email or SMS trigger before the drift becomes permanent.",
            "Run cross-sell and upsell campaigns — suggest complementary categories based on what they already buy.",
            "Offer a next-purchase discount with a short expiry (14 days) to create urgency.",
            "Introduce spend thresholds — bonus points or free shipping once they reach $1,500 in a rolling 90-day window.",
            "Send targeted messages referencing their past category preferences, not generic promotions.",
            "Goal: move at least 10% of this segment to 5+ orders within 6 months to graduate them to VIP Champions.",
        ],
        "kpi":    "Repeat purchase rate at 60-90 days. Target: at least 30% make a purchase within the window.",
        "budget": "Medium-high — highest conversion ROI potential after VIP Champions.",
    },
    {
        "raw_name":      "Low_Value & Inactive",  # CSV name is misleading — these are recent buyers
        "display":       "New One-Time Buyers",
        "priority":      3,
        "action":        "Convert",
        "color":         "#1D9E75",
        "customers_pct": "21.6%",
        "revenue_pct":   "3.7%",
        "median_recency":"29 days",
        "median_orders": "1",
        "median_spend":  "$328",
        "who_they_are": (
            "Customers who made their very first purchase in the last month (median 29 days ago) "
            "and have not come back yet. One order, $328 median spend. "
            "They are not inactive — the CSV label is incorrect. "
            "These customers are fresh and still within the critical post-purchase window "
            "where a single well-timed offer can convert them into repeat buyers. "
            "Treating them as inactive and ignoring them is the biggest missed opportunity."
        ),
        "actions": [
            "Launch a 3-step post-purchase email sequence on days 3, 10, and 21 after their first order.",
            "Offer a second-purchase incentive — 10-15% off within 30 days — while intent is still warm.",
            "Send product discovery content related to the category of their first purchase.",
            "Invite them to join the loyalty program immediately — early enrollment increases long-term retention.",
            "Set a 30-day internal alert: anyone who has not reordered by day 30 enters a stronger follow-up track.",
            "Remove non-responders from promotional campaigns after 45 days to avoid marketing fatigue.",
        ],
        "kpi":    "Second-purchase conversion rate within 60 days. Target: 25% or above (industry benchmark: 20-30%).",
        "budget": "Medium — low-cost email and automation; high potential value per converted customer.",
    },
    {
        "raw_name":      "VIP",               # CSV name is misleading — this is the most dormant group
        "display":       "Dormant One-Time Buyers",
        "priority":      4,
        "action":        "Win-back or Suppress",
        "color":         "#888780",
        "customers_pct": "24.4%",
        "revenue_pct":   "3.2%",
        "median_recency":"234 days",
        "median_orders": "1",
        "median_spend":  "$237",
        "who_they_are": (
            "Customers who bought exactly once, spent the least of any group ($237 median), "
            "and have been completely absent for approximately 8 months (median 234 days). "
            "Despite being labeled VIP in the source data, they are the opposite: "
            "the lowest-value, most disengaged segment. "
            "One visit, minimal spend, and 8 months of silence makes re-engagement highly unlikely. "
            "Any campaign to this group must be minimal in cost."
        ),
        "actions": [
            "Send one win-back email with a strong offer (20-25% discount and a clear time limit).",
            "Use a scarcity message in the subject line (e.g., Your discount expires in 48 hours) to maximize open rate.",
            "No paid ads and no SMS — the expected return does not justify the cost of expensive channels.",
            "If no response within 30 days, move to suppression list and stop all campaigns.",
            "Run this win-back attempt at most once per quarter — more frequent contact accelerates unsubscribes.",
            "Review what these customers purchased — if it was a one-off category, the churn was structural, not behavioral.",
        ],
        "kpi":    "Win-back rate from single campaign. Realistic target: 3-7%. Below 2% means full suppression.",
        "budget": "Minimal — email automation only; no paid or manual outreach.",
    },
]

# ==================================
# Page Header
# ==================================
st.title("Recommendations & Actions per Customer Segment")

st.markdown(
    """
    Based on RFM clustering, customers are divided into **4 behaviorally distinct segments**.
    Each segment has a different revenue impact, behavioral profile, and business priority.
    The recommendations below are grounded in the actual RFM characteristics of each group.
    """
)

st.divider()

# ==================================
# Section 1 — Segmentation Summary Table
# ==================================
st.subheader("1. Segmentation Summary")

summary_rows = [
    {
        "Priority":       seg["priority"],
        "Segment":        seg["display"],
        "Action":         seg["action"],
        "Customers":      seg["customers_pct"],
        "Revenue":        seg["revenue_pct"],
        "Median Recency": seg["median_recency"],
        "Median Orders":  seg["median_orders"],
        "Median Spend":   seg["median_spend"],
    }
    for seg in SEGMENTS
]

st.dataframe(
    pd.DataFrame(summary_rows),
    use_container_width=True,
    hide_index=True,
    column_config={
        "Priority": st.column_config.NumberColumn("Priority", width="small"),
    },
)

st.divider()

# ==================================
# Section 2 — Revenue vs Customer Share Chart
# ==================================
st.subheader("2. Revenue vs Customer Share")

chart_data = pd.DataFrame([
    {
        "Segment":   seg["display"],
        "Customers": float(seg["customers_pct"].strip("%")),
        "Revenue":   float(seg["revenue_pct"].strip("%")),
    }
    for seg in SEGMENTS
])

chart_long = chart_data.melt(
    id_vars=["Segment"],
    value_vars=["Customers", "Revenue"],
    var_name="Metric",
    value_name="Percentage",
)

col_chart, col_note = st.columns([2, 1])

with col_chart:
    fig = px.bar(
        chart_long,
        x="Segment",
        y="Percentage",
        color="Metric",
        barmode="group",
        title="Customer Share vs Revenue Share by Segment (%)",
        labels={"Percentage": "%", "Metric": ""},
        color_discrete_map={"Customers": "#d4d0c8", "Revenue": "#EF9F27"},
    )
    fig.update_layout(
        xaxis_tickangle=-15,
        legend_title_text="",
        margin=dict(t=50, b=80),
    )
    st.plotly_chart(fig, use_container_width=True)

with col_note:
    st.info(
        """
        **The key asymmetry**

        VIP Champions are 25% of customers
        but generate 73% of revenue.

        This means:

        - Losing 1 Champion costs roughly 3 average customers in revenue.
        - Retaining Champions is the single highest-ROI action.
        - Equal budget across all 4 segments is the wrong approach.
        """
    )

st.divider()

# ==================================
# Section 3 — Per-Segment Strategy Cards
# ==================================
st.header("3. Strategy per Segment")

for seg in SEGMENTS:
    with st.container(border=True):

        # Segment header
        title_col, badge_col = st.columns([3, 1])
        with title_col:
            st.subheader(f"{seg['display']} — {seg['action']}")
        with badge_col:
            st.markdown(f"**Priority {seg['priority']} of 4**")

        st.divider()

        # Who they are + RFM metrics
        desc_col, metrics_col = st.columns([3, 2])

        with desc_col:
            st.markdown("**Who they are**")
            st.markdown(seg["who_they_are"])

        with metrics_col:
            st.markdown("**Key RFM metrics**")
            r1, r2 = st.columns(2)
            r1.metric("Customers",       seg["customers_pct"])
            r2.metric("Revenue Share",   seg["revenue_pct"])

            r3, r4 = st.columns(2)
            r3.metric("Median Recency",  seg["median_recency"])
            r4.metric("Median Spend",    seg["median_spend"])

            st.metric("Median Orders",   seg["median_orders"])

        st.divider()

        # Actions
        st.markdown("**Recommended actions**")
        for action in seg["actions"]:
            st.markdown(f"- {action}")

        st.divider()

        # KPI and budget
        kpi_col, budget_col = st.columns(2)
        with kpi_col:
            st.markdown(f"**KPI to track:** {seg['kpi']}")
        with budget_col:
            st.markdown(f"**Campaign budget level:** {seg['budget']}")

    st.write("")  # spacing between cards

st.divider()

# ==================================
# Section 4 — Executive Takeaway
# ==================================
st.header("4. Executive Takeaway")

col_invest, col_control = st.columns(2)

with col_invest:
    st.success(
        """
        **Where to invest**

        VIP Champions (73.3% of revenue)
        — Loyalty programs, personalization, weekly churn monitoring.

        Promising Mid-Tier Regulars (19.7% of revenue)
        — Re-engagement campaigns, upsell offers, spend threshold incentives.

        New One-Time Buyers (3.7% of revenue)
        — Post-purchase automation and second-order discount within 30 days.
        """
    )

with col_control:
    st.warning(
        """
        **Where to control cost**

        Dormant One-Time Buyers (3.2% of revenue)
        — One quarterly win-back email only.
        No SMS, no paid ads, no manual outreach.
        Suppress non-responders after 30 days.

        Do not apply equal marketing spend across all 4 segments.
        The data is clear: budget should follow revenue concentration.
        """
    )
