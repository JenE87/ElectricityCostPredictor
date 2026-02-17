import streamlit as st

def page_project_hypothesis_body():
    """
    Render the Project Hypotheses and Validation page for non-technical users.
    """
    st.write("### Project Hypotheses & Validation")

    st.success(
        "**Hypothesis 1 - Site characteristics influence electricity cost**\n"
        "* **Outcome:** Supported\n"
        "* **What we found:** Electricity cost varies across different site profiles. "
        "Site scale and usage patterns are strongly linked to higher or lower costs."
    )

    st.success(
        "**Hypothesis 2 - Operational intensity is a strong cost driver**\n"
        "* **Outcome:** Supported\n"
        "* **What we found:** Sites that are used more intensively (e.g., higher utilisation or "
        "more occupants) tend to have higher electricity costs."
    )

    st.success(
        "**Hypothesis 3 - A regression model can predict electricity cost with acceptable accuracy**\n"
        "* **Outcome:** Supported\n"
        "* **What we found:** A predictive model can estimate monthly electricity cost well enough "
        "to be useful for planning and budgeting decisions."
    )

    st.write("---")

    if st.checkbox("Show how each hypothesis was validated (method summary)"):
        st.markdown(
            "**Hypothesis 1** was checked using exploratory analysis (distributions, comparisons, and relationships).\n\n"
            "**Hypothesis 2** was checked by focusing on indicators of operational intensity "
            "(e.g., utilisation and occupancy) and how they relate to electricity cost.\n\n"
            "**Hypothesis 3** was validated by training a regression model and evaluating its performance "
            "on a held-out test set. The model performance and feature importance are available on the "
            "**Model Performance** page."
        )

    st.caption(
        "The goal of this project is decision support for budgeting and planning. "
        "Predictions provide guidance, not guaranteed future bills."
    )