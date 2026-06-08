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

# ==================================
# Segment Configuration
#
# The cluster_name values in RFM_segments.csv are misleading — they were assigned
# in an earlier modelling iteration. The SEGMENT_CONFIG below maps each raw CSV
# name to its correct business label based on actual RFM statistics:
#
#   "Early Lifecycle"      — actual: median 10d recency, 7 orders, $2,708 spend
#                            correct label: VIP Champions
#
#   "Mid_Value"            — actual: median 71d recency, 3 orders, $1,013 spend
#                            correct label: Promising Mid-Tier Regulars
#
#   "Low_Value & Inactive" — actual: median 29d recency, 1 order, $328 spend
#                            correct label: New One-Time Buyers (recent, not inactive)
#
#   "VIP"                  — actual: median 234d recency, 1 order, $237 spend
#                            correct label: Dormant One-Time Buyers (not VIP)
#
# To update labels if the source CSV changes, edit SEGMENT_CONFIG only.
# All downstream display uses the "display" key — nothing else needs to change.
# ==================================

SEGMENT_CONFIG = {
    "Early Lifecycle": {
        "display":     "VIP Champions",
        "priority":    1,
        "color":       "#EF9F27",
        "description": (
            "Your most valuable customers. They purchase very frequently (median 7 orders), "
            "very recently (median 10 days ago), and spend the most by far (median $2,708). "
            "Despite representing only 25% of customers, they generate 73% of all revenue."
        ),
    },
    "Mid_Value": {
        "display":     "Promising Mid-Tier Regulars",
        "priority":    2,
        "color":       "#3266ad",
        "description": (
            "Repeat buyers with solid spending ($1,013 median) who are starting to drift — "
            "last purchase was 71 days ago on average. They have bought 3 times, "
            "showing clear loyalty potential that needs to be activated before they go cold."
        ),
    },
    "Low_Value & Inactive": {
        "display":     "New One-Time Buyers",
        "priority":    3,
        "color":       "#1D9E75",
        "description": (
            "Customers who made their first purchase very recently (median 29 days ago) "
            "but have not returned yet. One order, $328 median spend. "
            "They are still in the early decision window — the right offer now can "
            "turn them into repeat buyers."
        ),
    },
    "VIP": {
        "display":     "Dormant One-Time Buyers",
        "priority":    4,
        "color":       "#888780",
        "description": (
            "Customers who bought exactly once, spent very little ($237 median), "
            "and have been completely inactive for approximately 8 months (median 234 days). "
            "The combination of one visit, minimal spend, and long absence makes "
            "re-engagement highly unlikely. Only minimal-cost campaigns are justified."
        ),
    },
}

COLOR_MAP = {cfg["display"]: cfg["color"] for cfg in SEGMENT_CONFIG.values()}


# ==================================
# Data Loading
# ==================================

@st.cache_data
def load_data():
    rfm = pd.read_csv('data/Processed/4_Final_segments.csv')

    # Build group-level profile directly from RFM data.
    # Groups_profile.csv does not contain cluster_name, so we derive the profile here.
    profile = (
        rfm.groupby(["cluster", "cluster_name"])
        .agg(
            number_of_Customers =("CustomerID",               "count"),
            total_orders        =("Number_of_Orders",         "sum"),
            median_orders       =("Number_of_Orders",         "median"),
            total_spend         =("Total_Spend",              "sum"),
            median_spend        =("Total_Spend",              "median"),
            avg_recency_days    =("Days_Since_Last_Purchase",  "mean"),
            median_recency_days =("Days_Since_Last_Purchase",  "median"),
        )
        .reset_index()
    )

    total_customers = profile["number_of_Customers"].sum()
    total_revenue   = profile["total_spend"].sum()

    profile["customer_%"]         = (profile["number_of_Customers"] / total_customers * 100).round(1)
    profile["revenue_%"]          = (profile["total_spend"]         / total_revenue   * 100).round(1)
    profile["avg_recency_days"]   = profile["avg_recency_days"].round(0).astype(int)
    profile["median_recency_days"]= profile["median_recency_days"].round(0).astype(int)

    # Attach display name, priority, and color from config
    profile["display_name"] = profile["cluster_name"].map(
        lambda n: SEGMENT_CONFIG.get(n, {}).get("display", n)
    )
    profile["priority"] = profile["cluster_name"].map(
        lambda n: SEGMENT_CONFIG.get(n, {}).get("priority", 99)
    )
    profile = profile.sort_values("priority").reset_index(drop=True)

    # Mirror display name onto the customer-level table for chart use
    rfm["display_name"] = rfm["cluster_name"].map(
        lambda n: SEGMENT_CONFIG.get(n, {}).get("display", n)
    )

    return rfm, profile


rfm_model, groups_profile = load_data()

# ==================================
# Page Header
# ==================================
st.title("Customer Segmentation — RFM Groups")

st.markdown(
    """
    This page breaks down the **4 customer segments** identified by RFM clustering.
    Each segment has a distinct behavioral profile, revenue share, and business priority.
    """
)

st.divider()

# ==================================
# KPI Strip
# ==================================
k1, k2, k3, k4 = st.columns(4)
k1.metric("Total Customers",        f"{int(groups_profile['number_of_Customers'].sum()):,}")
k2.metric("Total Revenue",          f"${groups_profile['total_spend'].sum():,.0f}")
k3.metric("Number of Segments",     "4")
k4.metric("Revenue in Top Segment", f"{groups_profile['revenue_%'].max():.1f}%")

st.divider()

# ==================================
# Section 1 — Segment Profile Cards
# ==================================
st.subheader("1. Segment Profiles")

for _, row in groups_profile.iterrows():
    cfg = SEGMENT_CONFIG.get(row["cluster_name"], {})

    with st.container(border=True):
        col_desc, col_metrics = st.columns([2, 3])

        with col_desc:
            st.markdown(f"**{row['display_name']}**")
            st.caption(f"Priority {row['priority']} of 4")
            st.markdown(cfg.get("description", ""))

        with col_metrics:
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Customers",       f"{int(row['number_of_Customers']):,}",
                      f"{row['customer_%']}%")
            m2.metric("Revenue Share",   f"{row['revenue_%']}%")
            m3.metric("Median Recency",  f"{row['median_recency_days']}d")
            m4.metric("Median Spend",    f"${row['median_spend']:,.0f}")

            m5, m6 = st.columns(2)
            m5.metric("Median Orders",   f"{int(row['median_orders'])}")
            m6.metric("Avg Recency",     f"{row['avg_recency_days']}d")

st.divider()

# ==================================
# Section 2 — Group Summary Table
# ==================================
st.subheader("2. Group Summary Table")

# Select and rename columns for display — names are kept separate from formatting
# so any mismatch between the two is immediately visible.
summary_cols = {
    "display_name":          "Segment",
    "number_of_Customers":   "Customers",
    "median_orders":         "Median Orders",
    "median_spend":          "Median Spend ($)",
    "median_recency_days":   "Median Recency (days)",
    "avg_recency_days":      "Avg Recency (days)",
    "customer_%":            "Customer %",
    "revenue_%":             "Revenue %",
}

summary_display = (
    groups_profile[list(summary_cols.keys())]
    .rename(columns=summary_cols)
)

st.dataframe(
    summary_display.style.format({
        "Customers":              "{:,.0f}",
        "Median Orders":          "{:,.0f}",
        "Median Spend ($)":       "${:,.2f}",
        "Median Recency (days)":  "{:.0f}",
        "Avg Recency (days)":     "{:.0f}",
        "Customer %":             "{:.1f}%",
        "Revenue %":              "{:.1f}%",
    }),
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ==================================
# Section 3 — Revenue vs Customer Distribution
# ==================================
st.subheader("3. Revenue vs Customer Distribution")

pie_col1, pie_col2 = st.columns(2)

with pie_col1:
    fig_cust = px.pie(
        groups_profile,
        names="display_name",
        values="customer_%",
        title="Customer Distribution by Segment (%)",
        hole=0.45,
        color="display_name",
        color_discrete_map=COLOR_MAP,
    )
    fig_cust.update_traces(textposition="outside", textinfo="percent+label")
    fig_cust.update_layout(showlegend=False, margin=dict(t=50, b=20, l=20, r=20))
    st.plotly_chart(fig_cust, use_container_width=True)

with pie_col2:
    fig_rev = px.pie(
        groups_profile,
        names="display_name",
        values="revenue_%",
        title="Revenue Contribution by Segment (%)",
        hole=0.45,
        color="display_name",
        color_discrete_map=COLOR_MAP,
    )
    fig_rev.update_traces(textposition="outside", textinfo="percent+label")
    fig_rev.update_layout(showlegend=False, margin=dict(t=50, b=20, l=20, r=20))
    st.plotly_chart(fig_rev, use_container_width=True)

st.caption(
    "VIP Champions (25.2% of customers) generate 73.3% of revenue — "
    "a classic Pareto pattern. Every other segment combined accounts for the remaining 26.7%."
)

st.divider()

# ==================================
# Section 4 — Behavioral Distributions
# ==================================
st.subheader("4. RFM Behavioral Distributions by Segment")

tab_rec, tab_ord, tab_spend = st.tabs([
    "Recency (Days Since Last Purchase)",
    "Order Frequency",
    "Total Spend",
])

box_kwargs = dict(
    x="display_name",
    color="display_name",
    color_discrete_map=COLOR_MAP,
    points="outliers",
)

with tab_rec:
    fig_rec = px.box(
        rfm_model,
        y="Days_Since_Last_Purchase",
        title="Days Since Last Purchase by Segment",
        labels={
            "Days_Since_Last_Purchase": "Recency (Days)",
            "display_name":             "Segment",
        },
        **box_kwargs,
    )
    fig_rec.update_layout(showlegend=False, xaxis_title="Segment")
    st.plotly_chart(fig_rec, use_container_width=True)
    st.caption(
        "VIP Champions and New One-Time Buyers are the most recent purchasers. "
        "Dormant One-Time Buyers have not purchased in roughly 8 months — "
        "this extreme recency gap is what separates them from New One-Time Buyers, "
        "who also have 1 order but bought last month."
    )

with tab_ord:
    fig_ord = px.box(
        rfm_model,
        y="Number_of_Orders",
        title="Number of Orders by Segment",
        labels={"Number_of_Orders": "Orders", "display_name": "Segment"},
        **box_kwargs,
    )
    fig_ord.update_layout(showlegend=False, xaxis_title="Segment")
    st.plotly_chart(fig_ord, use_container_width=True)
    st.caption(
        "VIP Champions have by far the highest purchase frequency (median 7 orders). "
        "All other segments hover around 1-3 orders — "
        "recency and spend are the tiebreakers when frequency alone cannot separate groups."
    )

with tab_spend:
    fig_spd = px.box(
        rfm_model,
        y="Total_Spend",
        title="Total Spend ($) by Segment",
        labels={"Total_Spend": "Total Spend ($)", "display_name": "Segment"},
        **box_kwargs,
    )
    fig_spd.update_layout(showlegend=False, xaxis_title="Segment")
    st.plotly_chart(fig_spd, use_container_width=True)
    st.caption(
        "VIP Champions spend a median of $2,708 — more than 2.5x the Mid-Tier group. "
        "New One-Time Buyers ($328) and Dormant One-Time Buyers ($237) are close in spend "
        "but opposite in recency, which is why they require completely different strategies."
    )

st.divider()

# ==================================
# Section 5 — Customer Explorer
# ==================================
st.subheader("5. Customer Explorer")

st.markdown("Select a segment to view its top 10 customers by total spend.")

# Build reverse map: display name → raw cluster_name for filtering
reverse_map = {cfg["display"]: raw for raw, cfg in SEGMENT_CONFIG.items()}

selected_display = st.selectbox(
    "Segment:",
    options=[
        cfg["display"]
        for cfg in sorted(SEGMENT_CONFIG.values(), key=lambda x: x["priority"])
    ],
)

raw_cluster_name = reverse_map[selected_display]

top_customers = (
    rfm_model[rfm_model["cluster_name"] == raw_cluster_name]
    .sort_values("Total_Spend", ascending=False)
    .head(10)
)

st.dataframe(
    top_customers[[
        "CustomerID", "Number_of_Orders",
        "Total_Spend", "Days_Since_Last_Purchase",
    ]]
    .rename(columns={
        "CustomerID":               "Customer ID",
        "Number_of_Orders":         "Orders",
        "Total_Spend":              "Total Spend ($)",
        "Days_Since_Last_Purchase": "Days Since Last Purchase",
    })
    .style.format({
        "Total Spend ($)": "${:,.2f}",
        "Orders":          "{:,.0f}",
    }),
    use_container_width=True,
    hide_index=True,
)
