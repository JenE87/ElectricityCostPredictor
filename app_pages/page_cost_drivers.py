import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.data_management import (
    load_electricity_data, load_electricity_data_raw)


def page_cost_drivers_body():
    """
    Render the EDA & Cost Drivers page, readable for non-technical users with
    optional deeper detail.
    """
    st.write("### Electricity Cost Drivers Analysis")

    st.info(
        "**Business Requirement 1:** Understand which site and operational "
        "factors influence electricity cost."
    )

    st.write(
        "This page summarises the main cost drivers identified during "
        "analysis."
    )

    df = load_electricity_data()
    df_raw = load_electricity_data_raw()

    st.write("---")
    st.write("### Key Takeaways")

    st.success(
        "* Electricity cost generally increases with **site scale** and "
        "**operational intensity**.\n"
        "* The strongest drivers observed were typically **site area**, "
        "**water consumption**, **utilisation rate**, and **resident/occupant "
        "count**.\n"
        "* Some factors have weaker direct relationships, but still improve "
        "estimates when combined."
    )

    st.write("---")

    with st.expander("Explore the analysis", expanded=False):
        # Preview of dataset (no engineered/encoded columns)
        if st.checkbox("Inspect dataset preview"):
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

            st.caption(
                f"Dataset preview showing original fields "
                f"({df_raw.shape[0]:,} rows total):"
            )
            st.dataframe(df_raw[available_cols].head(10))

        if st.checkbox("Show correlation study (numeric features)"):
            st.caption(
                "Correlation values indicate how strongly variables are "
                "related (positive or negative). Values closer to 0 indicate "
                "a weaker relationship."
            )

            numeric_cols = (
                df
                .select_dtypes(include=["int64", "float64"])
                .columns
                .tolist()
            )

            corr = (
                df[numeric_cols]
                .corr(numeric_only=True)["electricity_cost"]
                .drop("electricity_cost")
                .sort_values(key=lambda s: s.abs(), ascending=False)
            )

            corr_df = corr.to_frame("correlation")

            styled_corr = corr_df.style.format(
                {"correlation": "{:.3f}"}
            )

            st.dataframe(styled_corr)

            st.write("#### Top correlated features")
            top_corr = corr.abs().head(8).sort_values()

            fig, axes = plt.subplots()
            axes.barh(top_corr.index, top_corr.values)
            axes.set_xlabel("Absolute correlation with electricity_cost")
            axes.set_ylabel("Feature")
            st.pyplot(fig)

        if st.checkbox("Show structure type distribution"):
            st.caption(
                "This shows how many sites of each structure type are in "
                "the dataset."
            )

            counts = df_raw["structure_type"].value_counts()

            fig, axes = plt.subplots(figsize=(6, 4))
            axes.bar(counts.index, counts.values)
            axes.set_title("Counts of Structure Type")
            axes.set_xlabel("Structure type")
            axes.set_ylabel("Number of sites")
            plt.xticks(rotation=45, ha="right")
            st.pyplot(fig)

        if st.checkbox(
            "Show electricity cost for sites with vs without residents"
        ):
            st.caption(
                "This compares electricity cost between sites that have "
                "residents and those that do not (e.g., commercial or "
                "industrial sites)."
            )

            df_plot = df_raw.copy()
            df_plot["Residents"] = df_plot["resident_count"].apply(
                lambda x: "No residents" if x == 0 else "Has residents"
            )

            fig, ax = plt.subplots(figsize=(6, 4))
            sns.boxplot(
                data=df_plot,
                x="Residents",
                y="electricity_cost",
                ax=ax
            )
            ax.set_title("Electricity Cost: Sites With vs Without Residents")
            ax.set_ylabel("Electricity cost (USD)")
            st.pyplot(fig)

        # Feature importance (Notebook 04 outputs)
        if st.checkbox("Show model-based cost drivers (feature importance)"):
            version = "v1"
            model_path = f"outputs/ml_pipeline/electricity_cost/{version}"

            st.caption(
                "This view shows which inputs the trained model relied on "
                "most when producing estimates."
            )

            feat_imp = pd.read_csv(f"{model_path}/feature_importance.csv")
            st.write("#### Feature importance table (top 10)")
            st.dataframe(feat_imp.head(10))

            st.image(
                f"{model_path}/feature_importance.png",
                caption="Feature importance (Random Forest)"
            )

        # Interactive relationship plot
        if st.checkbox("Explore relationships (scatter plot)"):
            st.caption(
                "Select a variable to see how it relates to electricity cost "
                "across sites."
            )

            candidates = [
                "site_area",
                "water_consumption",
                "utilisation_rate",
                "resident_count",
                "issue_resolution_time",
                "air_quality_index",
                "recycling_rate",
            ]
            available = [c for c in candidates if c in df.columns]

            feature = st.selectbox("Choose a variable", options=available)

            fig2, ax2 = plt.subplots()
            ax2.scatter(df[feature], df["electricity_cost"], alpha=0.4)
            ax2.set_xlabel(feature)
            ax2.set_ylabel("electricity_cost (USD)")
            st.pyplot(fig2)

    st.caption(
        "Plots show patterns in the dataset. They help identify associations, "
        "but do not necessarily imply causation."
    )
