import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.data_management import load_electricity_data, load_electricity_data_raw

def page_cost_drivers_body():
    """
    Render the EDA & Cost Drivers page, readable for non-technical users with optional deeper detail.
    """
    st.write("### EDA & Cost Drivers")

    st.info(
        "**Business Requirement 1:** Understand which site and operational factors influence electricity cost.\n\n"
        "This page summarises the main cost drivers identified during analysis."
    )

    df = load_electricity_data()
    df_raw = load_electricity_data_raw()

    st.write("---")
    st.write("### Key Takeaways")

    st.success(
        "* Electricity cost generally increases with **site scale and operational intensity**.\n"
        "* The strongest drivers observed were typically **site area**, **water consumption**, "
        "**utilisation rate**, and **resident/occupant count**.\n"
        "* Some factors have weaker direct relationships, but still improve estimates when combined." 
    )

    st.write("---")

    if st.checkbox("Inspect dataset preview"):
        # Base cols (no engineered/encoded columns)
        base_cols = [
            "site_area",
            "structure_type",
            "water_consumption",
            "recycling_rate",
            "utilisation_rate",
            "air_quality_index",
            "issue_resolution_time",
            "resident_count",
            "electricity_cost",
        ]

        available_cols = [c for c in base_cols if c in df_raw.columns]
    
        st.write(
            f"Dataset preview showing original fields "
            f"({df_raw.shape[0]:,} rows total):"
        )
        st.dataframe(df_raw[available_cols].head(10))
    
    st.write("---")

