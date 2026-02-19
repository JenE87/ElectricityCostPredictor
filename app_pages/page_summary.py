import streamlit as st
from src.data_management import load_electricity_data


def page_summary_body():
    """
    Render the Quick Project Summary page for non-technical users.
    """
    st.write("### Quick Project Summary")

    st.info(
        "**What this project does**\n"
        "* This dashboard helps estimate **monthly electricity cost (USD)** "
        "for a site.\n"
        "* It uses patterns learned from historical site data to support "
        "**budgeting and planning**.\n\n"
        "**Who it is for**\n"
        "* A facilities or cost manager who needs quick, consistent cost "
        "estimates for different site profiles.\n\n"
        "**What you can do in this dashboard**\n"
        "* Review the main factors associated with higher/lower electricity "
        "costs.\n"
        "* Enter site details and receive an estimated monthly electricity "
        "cost."
    )

    st.write(
        "For full project documentation and further information, please visit "
        "and read the [Project README file]("
        "https://github.com/JenE87/ElectricityCostPredictor)."
    )

    st.write("---")

    st.success(
        "**Business requirements**\n"
        "* **BR1:** Identify which site characteristics and operational "
        "factors influence electricity cost.\n"
        "* **BR2:** Provide a prediction tool that estimates monthly "
        "electricity cost for a given site profile."
    )

    st.write("---")
    st.write("### Dataset Snapshot")

    df = load_electricity_data()
    min_cost = df["electricity_cost"].min()
    med_cost = df["electricity_cost"].median()
    max_cost = df["electricity_cost"].max()

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container():
            st.metric(
                "Number of sites",
                f"{df.shape[0]:,}"
            )

    with col2:
        with st.container():
            st.metric(
                "Observed cost range (monthly)",
                f"${min_cost:,.0f} – ${max_cost:,.0f}"
            )

    with col3:
        with st.container():
            st.metric(
                "Typical monthly cost (median)",
                f"${med_cost:,.0f}"
            )

    st.write("---")
    st.write("### Key Dataset Variables used for Estimation")

    st.markdown(
        "* **Site area** (m²)\n"
        "* **Structure type** (Residential / Commercial / Mixed-use / "
        "Industrial)\n"
        "* **Water consumption** (liters/day)\n"
        "* **Utilisation rate** (%)\n"
        "* **Resident / occupant count**\n"
        "* **Issue resolution time** (hours)\n"
        "* **Recycling rate** (%)\n"
        "* **Air quality index** (AQI)"
    )

    st.write("---")
    st.write("### Project Terms & Jargon")

    st.info(
        "- **Electricity cost:** the estimated monthly spend on electricity "
        "for a site.\n"
        "- **Site profile:** a set of site details (e.g., size, type, "
        "utilisation) used to estimate cost.\n"
        "- **Cost drivers:** factors that are commonly associated with higher "
        "or lower electricity cost.\n"
        "- **Prediction:** an estimate based on patterns from historical data."
    )

    st.caption(
        "This dashboard provides estimates based on patterns in the dataset. "
        "Actual costs may differ due to tariffs, weather, equipment "
        "efficiency, and other external factors."
    )
