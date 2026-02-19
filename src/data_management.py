import joblib
import pandas as pd
import streamlit as st


@st.cache_data
def load_electricity_data_raw():
    """
    Load the raw dataset for non-technical preview purposes,
    and standardise column names (including fixing known typos).
    """
    file_path = "inputs/datasets/raw/electricity_cost_dataset.csv"

    try:
        df = pd.read_csv(file_path)
        if df.empty:
            st.error("Raw dataset is empty.")
            st.stop()

        df.columns = (
            df.columns.str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        rename_map = {
            "site_area": "site_area",
            "structure_type": "structure_type",
            "water_consumption": "water_consumption",
            "recycling_rate": "recycling_rate",
            "utilisation_rate": "utilisation_rate",
            "air_qality_index": "air_quality_index",            # raw data typo
            "issue reolution time": "issue_resolution_time",    # raw data typo
            "resident_count": "resident_count",
            "electricity_cost": "electricity_cost",
        }

        valid_renames = {
            k: v for k, v in rename_map.items() if k in df.columns
        }

        df = df.rename(columns=valid_renames)

        return df

    except FileNotFoundError:
        st.error(f"Raw dataset file not found at `{file_path}`.")
        st.stop()

    except Exception as e:
        st.error(f"Unexpected error while loading raw dataset:\n\n{e}")
        st.stop()


def load_electricity_data():
    """
    Load the cleaned dataset with standardised names and basic error handling.
    """
    file_path = "outputs/datasets/cleaned/ElectricityCostCleaned.csv"

    try:
        df = pd.read_csv(file_path)
        if df.empty:
            st.error(
                "Dataset is empty. Please rerun Notebook 01 (Data Collection)."
            )
            st.stop()
        return df

    except FileNotFoundError:
        st.error(
            f"Dataset file not found at `{file_path}`.\n\n"
            "Please run Notebook 01 (Data Collection) first."
        )
        st.stop()

    except Exception as e:
        st.error(f"Unexpected error while loading dataset:\n\n{e}")
        st.stop()


def load_pkl_file(file_path: str):
    """Load a pickle file (model/features) with error handling."""
    try:
        return joblib.load(file_path)

    except FileNotFoundError:
        st.error(
            f"File not found at `{file_path}`.\n\n"
            "Please run Notebook 04 (Modelling & Evaluation)."
        )
        st.stop()

    except Exception as e:
        st.error(f"Unexpected error while loading file:\n\n{e}")
        st.stop()
